import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.weathersa.co.za/')
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find
todayCast = soup.find(class_="panel panel-default").get_text()
days = soup.find(class_='weather').get_text()
citytables = soup.find(class_="col-sm-7 topCities").get_text()
Alerts = soup.find(class_="tab-content").get_text()

print(todayCast)
print(days)
print(citytables)
print(Alerts)
