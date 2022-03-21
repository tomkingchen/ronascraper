# app.py
import requests
from bs4 import BeautifulSoup

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    scrap_result = 'Not available'
    URL = 'https://covidlive.com.au/report/daily-summary/vic'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    page_content = soup.find(id='content')
    daily_summary_table = page_content.find('table', class_='DAILY-SUMMARY')
    notchecked = True
    for daily_summary_tr in daily_summary_table.find_all('tr')[1:]:
        daily_numbers = daily_summary_tr.find('td', class_='COL1 CATEGORY')
        daily_numbers = daily_numbers.text.strip()
        # if daily_numbers == "New Cases" and notchecked:
        #     daily_newcases = daily_summary_tr.find('td', class_='COL2 TOTAL')
        #     scrap_result = daily_newcases.text.strip()
        #     notchecked = False
        # elif daily_numbers == "Cases" and notchecked :
        #     daily_newcases = daily_summary_tr.find('td', class_='COL4 NET')
        #     scrap_result = daily_newcases.text.strip()
        #     notchecked = False
        if daily_numbers == "Hospitalised" and notchecked:
            daily_hosp_number = daily_summary_tr.find('td', class_='COL2 TOTAL')
            scrap_result = daily_hosp_number.text.strip()

    return "<head><style>p.bignumber { font-size: 330px;}</style></head><body><p class=\"bignumber\">" + scrap_result + "</p></body>"