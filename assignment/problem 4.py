import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Find the table element containing the data
table = soup.find('table',id='main_table_countries_today')
# Extracting the table headers
headers = [th.text for th in table.find_all('th')]
# Extract the table rows
rows = []
for tr in table.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all('td')]
    if row:
        rows.append(row)
# Converting the data into a Pandas dataframe
df = pd.DataFrame(rows, columns=headers)
# Selecting the desired columns
columns_to_keep = ['Country,Other', 'Continent', 'Population', 'TotalCases', 'NewCases',
                   'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases']
df = df[columns_to_keep]
print(df)


