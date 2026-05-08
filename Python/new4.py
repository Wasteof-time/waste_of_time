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
        # print(text)

    else:
        text = ""
        print(f"Failed: {response.status_code}")


    match = re.search(r"Examination Results[\s\xa0]+March 2026\s+([A-Z][A-Z\s]+?)[\s\xa0]+\(\s*(\d+)\s*[\r\n\t\s]*\)",text)
    student_name = match.group(1).strip() if match else ""
    roll_no      = match.group(2).strip() if match else ""

    practical_subjects = re.findall(
        r"(SCIENCE|SOCIAL SCIENCE)\s+\d+\s+(\d+)\s+(\d+)\s+(\d+)\s+P", text
    )

    theory_subjects = re.findall(
        r"(TAMIL|ENGLISH|MATHS)\s+\d+\s+(\d+)\s+(\d+)\s+P", text
    )

    total = re.search(r"TOTAL\s+0*(\d+)", text).group(1)

    result = [["NAME" , student_name ] ,["ROLLNO" , roll_no]]

    subject_marks = {}
    for subj, theory, total_mark in theory_subjects:
        subject_marks[subj] = int(total_mark)

    for subj, theory, pra, total_mark in practical_subjects:
        subject_marks[subj] = int(total_mark)

    order = ["TAMIL", "ENGLISH", "MATHEMATICS" , "SCIENCE", "SOCIAL SCIENCE"]
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