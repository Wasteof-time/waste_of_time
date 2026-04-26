import requests
from bs4 import BeautifulSoup

BASE_URL = "http://tnresults.nic.in"
FORM_URL  = f"{BASE_URL}/"
POST_URL  = f"{BASE_URL}/2026_9994hsc.asp"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-IN,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": FORM_URL,
    "Origin": BASE_URL,
}


def fetch_result(regno: str, dob: str) -> None:
    """
    regno : 7-digit registration number as string
    dob   : date of birth in dd/mm/yyyy format
    """
    session = requests.Session()
    session.headers.update(HEADERS)

    # Step 1: GET the form page to pick up any session cookies
    print("[*] Fetching form page...")
    try:
        session.get(FORM_URL, timeout=10)
    except Exception as e:
        print(f"[!] Could not reach form page: {e}")
        print("[*] Proceeding anyway...")

    # Step 2: POST with credentials
    payload = {
        "regno": regno.strip(),
        "dob":   dob.strip(),
        "B1":    "Get Marks",
    }

    print(f"[*] Submitting for regno={regno}, dob={dob} ...")
    try:
        resp = session.post(POST_URL, data=payload, timeout=15, allow_redirects=True)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"[!] HTTP error: {e}")
        return
    except requests.exceptions.ConnectionError:
        print("[!] Could not connect. Check the domain/URL.")
        return
    except requests.exceptions.Timeout:
        print("[!] Request timed out.")
        return

    if resp.status_code != 200:
        print(f"[!] Unexpected status: {resp.status_code}")
        return

    # Step 3: Parse
    parse_result(resp.text)


def parse_result(html: str) -> None:
    soup = BeautifulSoup(html, "html.parser")

    # Check for error messages (no result / wrong input)
    body_text = soup.get_text(separator=" ", strip=True)
    error_keywords = ["invalid", "not found", "no record", "wrong", "incorrect"]
    if any(kw in body_text.lower() for kw in error_keywords):
        print("[!] Server returned an error or no record found:")
        print(body_text[:500])
        return

    print("\n" + "="*60)
    print("                      RESULT")
    print("="*60)

    tables = soup.find_all("table")
    if not tables:
        print("[!] No tables found in response. Raw HTML saved to result.html")
        with open("result.html", "w", encoding="utf-8") as f:
            f.write(html)
        return

    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all(["td", "th"])
            if not cols:
                continue
            parts = [c.get_text(separator=" ", strip=True) for c in cols]
            # skip empty/whitespace-only rows
            if any(p for p in parts):
                print("  |  ".join(parts))
        print()  # blank line between tables

    print("="*60)

    # Also save full HTML in case you want to inspect it
    with open("result.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("[*] Full result page saved to result.html")


if __name__ == "__main__":
    regno = input("Enter Registration No (7 digits): ").strip()
    dob   = input("Enter Date of Birth (dd/mm/yyyy): ").strip()
    fetch_result(regno, dob)