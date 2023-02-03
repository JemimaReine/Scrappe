import requests
from bs4 import BeautifulSoup
import urllib.request


url = 'https://www.jumia.ci/electronique/'
BASE = "https://www.jumia.ci"
j = 0
while url:
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find_all('div', class_="-paxs row _no-g _4cl-3cm-shs")
    for i in div:
        articles = i.find_all('article')
        for article in articles:
            if article.find('a').get('href'):
                url_article = BASE + article.find('a').get('href')
                response_article = requests.get(url_article)
                details = response_article.content
                soup_article = BeautifulSoup(details, 'html.parser')
                name = soup_article.find('h1', class_='-fs20 -pts -pbxs').contents

                #
                if soup_article.find('span', class_='-b -ltr -tal -fs24'):
                    prix_promotionnel = soup_article.find('span', class_='-b -ltr -tal -fs24').contents
                else:
                    prix_promotionnel = ""

                #  Recuperation du prix réel de l'article
                if soup_article.find('span', class_='-tal -gy5 -lthr -fs16'):
                    prix_reel = soup_article.find('span', class_='-tal -gy5 -lthr -fs16').contents
                else:
                    prix_reel = ''

                if soup_article.find('span', class_='bdg _dsct _dyn -mls'):
                    promotion = soup_article.find('span', class_='bdg _dsct _dyn -mls').contents
                else:
                    promotion = ''
                if soup_article.find('div', class_='markup -mhm -pvl -oxa -sc'):
                    description = soup_article.find('div', class_='markup -mhm -pvl -oxa -sc').text
                else :
                    description = ""

                if soup_article.find('img', class_='-fw -fh'):
                    image = soup_article.find('img', class_='-fw -fh').get('src')
                    urllib.request.urlretrieve(image, name[0][0:10] + '.jpg')
                else :
                    image = ""

            break
    if soup.find('a', attrs={'aria-label' : "Page suivante"}):
        url = BASE + soup.find('a', attrs={'aria-label' : "Page suivante"}).get('href')
        print(url)
    else:
        url = False
    j = j + 1
    print(j)


