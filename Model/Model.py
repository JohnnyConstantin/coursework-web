from flask import request, Flask, render_template, request, jsonify, make_response
import requests
from bs4 import BeautifulSoup

#Model for processing data and returning to controller
class Model():

    def __init__(self, item, d):
        self.item = item
        self.d = d

    def parse_mobicom(self, item, d):
        # get pages
        for j in range(0, 500, 12):
            url = 'https://www.mobicomshop.ru/noutbuki/'
            # указываем get параметр с помощью которого определяется номер страницы
            par = {'start': j}
            # записываем ответ сервера в переменную r
            session = requests.Session()
            r = session.get(url, params=par)
            # получаем объект  BeautifulSoup и записываем в переменную soup
            soup = BeautifulSoup(r.text, 'html.parser')
            # с помощью цикла перебираем товары на странице и получаем из них нужные параметры
            for i in range(12):
                # получаем название товара
                product = soup.find_all(class_='prod-en-lista-name')[i].get_text()
                if item in product:
                    # Получаем заголовок
                    naming = soup.find_all(class_='prod-en-lista-name')[i].a.get_text()
                    # получаем цену товара
                    price = soup.find_all(class_='buttonprice-list')[i].get_text()
                    # получаем картинку
                    image = soup.find_all(class_='jshop_img')[i]['src']
                    # получаем ссылку
                    href = soup.find_all(class_='prod-list-detail')[i]['href']
                    href = 'https://www.mobicomshop.ru' + href.replace(".html", "")

                    # удаляем пробел из цены
                    price = price.replace("\n", "")
                    # добавляем данные о товаре в список
                    d.append([naming, price, image, href, "mobicom"])


    def parse_kns(self, item, d):
        # get pages
        for j in range(30):
            url = 'https://www.kns.ru/catalog/noutbuki/'
            # указываем get параметр с помощью которого определяется номер страницы
            par = url + f"/page{j}/"
            # записываем ответ сервера в переменную r
            session = requests.Session()
            r = session.get(par)
            # получаем объект  BeautifulSoup и записываем в переменную soup
            soup = BeautifulSoup(r.text, 'html.parser')
            # с помощью цикла перебираем товары на странице и получаем из них нужные параметры
            for i in range(30):
                # получаем название товара
                product = soup.find_all(class_='name d-block')[i]['title']
                if item in product:
                    # получаем цену товара
                    price = soup.find_all(class_='price my-1')[i].get_text()
                    # получаем картинку
                    image = soup.find_all('img')[i]['src']
                    # получаем ссылку
                    href = soup.find_all(class_='name d-block')[i]['href']
                    href = 'https://www.kns.ru' + href

                    # удаляем пробел из цены
                    price = price.replace("\n", "")
                    # добавляем данные о товаре в список
                    d.append([product, price, image, href, "kns"])