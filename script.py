import requests
from bs4 import BeautifulSoup
import pyodbc


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=PCJEMI05\SQLEXPRESS;"
                      "Database=dbScrapper;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()


url = 'https://www.jumia.ci/index/allcategories/'
url2 = ''
BASE = "https://www.jumia.ci"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

#Categories = []
Produits = []

divs = soup.find_all('div', class_="itm col")
for div in divs:
    links = div.find_all('a', class_="data-name")
    for link in links:
        Produits.append(link.text)
        print(Produits)


for prodNom in Produits:
     cursor.execute("INSERT INTO Produit (produitNom) VALUES (?)", prodNom)
     conn.commit()



# categories = soup.find_all("a", class_="-pbm -m -upp -hov-or5")
# for category in categories:
#     Categories.append(category.text)




# for tagNom in Tags:
#     cursor.execute("INSERT INTO Tag (tagNom) VALUES (?)", tagNom)
#     conn.commit()
# for cateNom in Categories:
#     cursor.execute("INSERT INTO Categories (categorieNom) VALUES (?)", cateNom)
# conn.commit()

# Step 4: Close connection
conn.close()
