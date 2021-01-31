from bs4 import BeautifulSoup
import requests


html_Text = requests.get("https://www.worldremit.com/en/morocco?transfer=bnk").text
soup = BeautifulSoup(html_Text,'lxml')

jobs = soup.find_all(("div", {"class": "MuiCollapse-container MuiCollapse-entered"}))

Dirham = jobs.find(("div"))

print(Dirham)
# print(jobs)

