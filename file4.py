import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")


table = soup.find("table", id="main_table_countries_today")


header_row = table.find("thead").find_all("tr")[0]
headers = [header.text.strip() for header in header_row.find_all("th")]

data_rows = []
body = table.find("tbody")
rows = body.find_all("tr")
for row in rows:
    data_cells = row.find_all("td")
    row_data = [cell.text.strip() for cell in data_cells]
    data_rows.append(row_data)

df = pd.DataFrame(data_rows, columns=headers)


selected_columns = [
    "Country,Other", "Continent", "Population",
    "TotalCases", "NewCases", "TotalDeaths",
    "NewDeaths", "TotalRecovered", "NewRecovered", "ActiveCases"
]
df = df[selected_columns]


print(df.head())
