import requests
from bs4 import BeautifulSoup

BASE_URL = "https://tnresults.nic.in/2026_HSCtnresults/2026_5341hsc.htm"

response = requests.get(BASE_URL)

if response.status_code == 200:
    html_content = response.text
    print(html_content)


else : 
    print("FUCK YOU MF")

