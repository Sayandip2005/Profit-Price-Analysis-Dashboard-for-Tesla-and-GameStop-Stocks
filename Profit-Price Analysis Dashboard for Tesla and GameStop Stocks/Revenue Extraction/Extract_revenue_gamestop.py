import requests
from bs4 import BeautifulSoup
import pandas as pd

html_data_2=requests.get(" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html").text
soup=BeautifulSoup(html_data_2,'html.parser')
gme_revenue=pd.DataFrame(columns=['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col=row.find_all("td")
    date=col[0].text
    revenue=col[1].text
    gme_revenue=pd.concat([gme_revenue, pd.DataFrame({"Date":[date],"Revenue":[revenue]})],ignore_index=True)


gme_revenue["Revenue"]=gme_revenue['Revenue'].str.replace('$',"")
gme_revenue["Revenue"]=gme_revenue['Revenue'].str.replace(',',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print(gme_revenue.tail())