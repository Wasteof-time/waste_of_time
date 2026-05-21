import requests
from bs4 import BeautifulSoup
import csv
import time
import re

f = open("C:\\Users\\Asus\\Desktop\\roll.csv" , "r")
f = csv.reader(f)
f = list(f)

g = open("data.csv" , "w")
g = csv.DictWriter(g , fieldnames=["NAME" , "ROLLNO" ,  "TAMIL", "ENGLISH", "MATHS" ,"SCIENCE" , "SOCIAL SCIENCE" ,  "TOTAL"])
g.writeheader()

for i in f:
    BASE_URL = "https://tnresults.nic.in/2026_SSLCtnresults/2026_8022sslc.htm"
    POST_URL = "https://tnresults.nic.in/2026_SSLCtnresults/2026_7669sslc.asp"

    REGNO = i[0]
    DOB   = i[1]

    print(f"{REGNO} : {DOB} doing this ")

    session = requests.Session()
    session.get(BASE_URL, headers={"User-Agent": "Mozilla/5.0"})
    payload = {
        "regno": REGNO,
        "dob":   DOB,
        "B1":    "Get Marks",
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer":    BASE_URL,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = session.post(POST_URL, data=payload, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        print(text)

    else:
        text = ""
        print(f"Failed: {response.status_code}")


    match = re.search(r"Examination Results[\s\xa0]+March 2026\s+([A-Z][A-Z\s]+?)[\s\xa0]+\(\s*(\d+)\s*[\r\n\t\s]*\)",text)
    student_name = match.group(1).strip() if match else ""
    roll_no      = match.group(2).strip() if match else ""

    # ── FIXED REGEX ────────────────────────────────────────────────────────────
    # Scraped text has subject name on one line and marks on the next line.
    # SCIENCE is special: "SCIENCE ( Theory  + Practical )\n( 074 + 025 )   099"

    def get_mark(subject, t):
        m = re.search(rf'(?<!\w){re.escape(subject)}\s*\n\s*(\d+)', t)
        return int(m.group(1)) if m else 0

    science_match = re.search(
        r'SCIENCE\s*\(.*?Theory.*?Practical.*?\)\s*\n.*?\)\s+(\d+)',
        text, re.IGNORECASE
    )

    subject_marks = {
        "TAMIL":          get_mark("TAMIL", text),
        "ENGLISH":        get_mark("ENGLISH", text),
        "MATHS":          get_mark("MATHS", text),
        "SCIENCE":        int(science_match.group(1)) if science_match else 0,
        "SOCIAL SCIENCE": get_mark("SOCIAL SCIENCE", text),
    }

    total_match = re.search(r'TOTAL\s*\n\s*(\d+)', text)
    total = total_match.group(1) if total_match else 0
    # ── END FIXED REGEX ────────────────────────────────────────────────────────

    result = [["NAME" , student_name ] ,["ROLLNO" , roll_no]]

    order = ["TAMIL", "ENGLISH", "MATHS" , "SCIENCE", "SOCIAL SCIENCE"]
    for subj in order:
        try :
            result.append((subj, subject_marks[subj]))
        except : 
            result.append((subj , 0))

    result.append(("TOTAL", int(total)))

    dictas = {}
    for k , v in result : 
        dictas[k] = v

    print(dictas)
    g.writerow(dictas)