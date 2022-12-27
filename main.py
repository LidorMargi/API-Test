import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_animal_names"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table", {"class":"wikitable sortable"})[1].tbody #on this page there are 2 tables from tha same class, I needed the 2nd
rows = table.find_all("tr") #find all rows and put them on a list
columns = [v.text for v in rows[0].find_all("th")] #find all columns names and put them on a list

for i in range(1, len(rows)):
    tds = rows[i].find_all("td")
    if len(tds) == 7:
        values = [tds[0].text, tds[5].get_text(separator=", ").strip()]
    else:
        continue
        
    print(values)

