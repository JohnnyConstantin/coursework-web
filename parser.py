from flask import request, Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def parse_mobicom(item):
    #For data
    d = []

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
        # с помощью циклам перебiраем товары на странице и получаем из них нужные параметры
        for i in range(12):
            # получаем название товара
            product = soup.find_all(class_='prod-en-lista-name')[i].get_text()
            if(item in product):
                # получаем цену товара
                price = soup.find_all(class_='prod-en-lista-price')[i].get_text()
                # удаляем пробел из цены
                price = price.replace(" ", "")
                price = price.replace("\n", "")
                # получаем ссылку на товар
                # добавляем данные о товаре в список
                d.append([product, price])
    for a in d:
        print(a, end='\n')

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/get_laptops', methods=['POST'])
def get_laptops():
    #here will be parsing
    checked = request.form.get('laptop')
    item = request.form.get('item_to_search')
    print(checked)
    parse_mobicom(item)

    return render_template('index.html')
