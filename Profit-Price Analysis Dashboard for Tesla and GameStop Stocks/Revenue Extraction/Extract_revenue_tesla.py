import requests
from bs4 import BeautifulSoup
import pandas as pd

html_data=requests.get(" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm").text
soup=BeautifulSoup(html_data,'html.parser')
tesla_revenue=pd.DataFrame(columns=['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col=row.find_all("td")
    date=col[0].text
    revenue=col[1].text
    tesla_revenue=pd.concat([tesla_revenue, pd.DataFrame({"Date":[date],"Revenue":[revenue]})],ignore_index=True)


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.head(10))