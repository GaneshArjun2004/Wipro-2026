import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

title = soup.title.string

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

table_data = []

table = soup.find("table")
rows = table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")
    table_data.append({
        "Company": cols[0].text.strip(),
        "Contact": cols[1].text.strip(),
        "Country": cols[2].text.strip()
    })

data = {
    "title": title,
    "links": links,
    "table_data": table_data
}

with open("html_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("HTML data extracted and saved successfully")
