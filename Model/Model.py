import requests
from bs4 import BeautifulSoup
#Model for processing data and returning to controller
class Model():

    def __init__(self, item, d):
        self.item = item
        self.d = d

    def parse_mobicom(self, item, d):
        for j in range(0, 500, 12):
            url = 'https://www.mobicomshop.ru/noutbuki/'
            par = {'start': j}
            session = requests.Session()
            r = session.get(url, params=par)
            soup = BeautifulSoup(r.text, 'html.parser')
            for i in range(12):
                product = soup.find_all(class_='prod-en-lista-name')[i].get_text()
                if item in product:
                    naming = soup.find_all(class_='prod-en-lista-name')[i].a.get_text()
                    price = soup.find_all(class_='buttonprice-list')[i].get_text()
                    image = soup.find_all(class_='jshop_img')[i]['src']
                    href = soup.find_all(class_='prod-list-detail')[i]['href']
                    href = 'https://www.mobicomshop.ru' + href.replace(".html", "")
                    price = price.replace("\n", "")
                    d.append([naming, price, image, href, "mobicom"])


    def parse_kns(self, item, d):
        for j in range(30):
            url = 'https://www.kns.ru/catalog/noutbuki/'
            par = url + f"/page{j}/"
            session = requests.Session()
            r = session.get(par)
            soup = BeautifulSoup(r.text, 'html.parser')
            for i in range(30):
                product = soup.find_all(class_='name d-block')[i]['title']
                if item in product:
                    price = soup.find_all(class_='price my-1')[i].get_text()
                    image = soup.find_all('img')[i]['src']
                    href = soup.find_all(class_='name d-block')[i]['href']
                    href = 'https://www.kns.ru' + href
                    price = price.replace("\n", "")
                    d.append([product, price, image, href, "kns"])