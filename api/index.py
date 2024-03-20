from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import math

app = Flask(__name__)

print('___api started____')

@app.route('/api/consultproduct', methods=['GET'])
def consulting_product():
    try:
        base_url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number=1&page_size=20&facet_filters=&sort=price'

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

        session = HTMLSession()
        site = session.get(base_url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        produtos = soup.find_all('div', class_=re.compile('productCard'))
        for produto in produtos:
                marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                preco = produto.find('span', class_=re.compile('priceCard')) .get_text().strip()
    
                print(marca)
                print(preco)
         
        '''
        qtd_items = soup.find('div', id="listingCount").get_text().strip()
        index = qtd_items.find(' ')
        qtd = qtd_items[:index]

        ultima_pagina = math.ceil(int(qtd)/ 20)
        dic_produtos = {'marca': [], 'preço': []}

        for i in range(1 , ultima_pagina + 1):
            url_pag = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
            site = requests.get(url_pag, headers=headers)
            soup = BeautifulSoup(site.content, 'html.parser')
            produtos = soup.find_all('div', class_=re.compile('productCard'))

            for produto in produtos:
                marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                ##preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

                print(marca)
        '''

        return jsonify({
            'status': 200,
            'message': 'final da chamada api',
        })
    except error as error:
         print(error)

if __name__ == '__main__':
    app.run( port=5000)