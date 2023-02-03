import requests
from bs4 import BeautifulSoup

# Envoyer une demande pour obtenir le code HTML de la page
url = "https://www.jumia.ci/index/allcategories/"
page = requests.get(url)

# conn = pyodbc.connect(
#     "Driver ={ODBC Driver 17 for SQL Server};"
#     "Server=PCJEMI05\SQLEXPRESS;"
#     "Database= dbScrapper;"
#     "Trusted_Connection=yes;"
# )
# cursor = conn.cursor()

# cursor.execute("CREATE TABLE Categorie(categorieName varchar(255))")



# Analyser le code HTML avec BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

categories = soup.find_all("a", class_="itm")
for category in categories:
    category_title = category.find_all("span", class_="text")
    # articles = category.find_all("article", class_="name")
    print("Category:", category_title)
    # for article in articles:
    #     print(" -", article.text)
# Trouver tous les éléments qui représentent les catégories sur la page

# articles = soup.find_all("h2", class_="article-title")

# product_title = soup.find("h1", class_="product-title").text
# product_price = soup.find("span", class_="product-price").text

#jm > main > div.row.-pvm > div:nth-child(4) > section > div > div > div:nth-child(1) > article

