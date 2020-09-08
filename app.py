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
    for daily_summary_tr in daily_summary_table.find_all('tr')[1:]:
        daily_newcases_cat = daily_summary_tr.find('td', class_='COL1 CATEGORY')
        daily_newcases_cat = daily_newcases_cat.text.strip()
        if daily_newcases_cat == "New Cases":
            daily_newcases = daily_summary_tr.find('td', class_='COL2 TOTAL')
            scrap_result = daily_newcases.text.strip()
    return "<font size=3000>" + scrap_result + "</font>"