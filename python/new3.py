import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_url(i):
    url = f"https://tnresults.nic.in/2026_SSLCtnresults/2026_{i}sslc.htm"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return (i, url)
    except requests.RequestException:
        pass
    return None

# Use threads to check all 9000 URLs concurrently
with ThreadPoolExecutor(max_workers=50) as executor:
    futures = {executor.submit(check_url, i): i for i in range(1000, 10000)}
    for future in as_completed(futures):
        result = future.result()
        if result:
            print(f"✅ Found valid URL: {result[1]}")
            break  # Remove this if you want to scan all