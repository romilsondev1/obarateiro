from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import math

app = Flask(__name__)

print('___api started____')

@app.route('/api/consultproduct', methods=['GET'])
def consulting_product():
    try:
        #started navegation
        #chrome_options = webdriver.ChromeOptions()
        #desabled open to navigation
        #chrome_options.add_argument('--headless=new')
        #configure service
        #chrome_service = webdriver.ChromeService(executable_path='/Users/[...]binaries(117)/chromedriver')
        #configure driver
        driver = webdriver.Chrome()

        base_url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number=1&page_size=20&facet_filters=&sort=price'

        #start navegation
        driver.get(base_url)

        page = driver.page_source.encode('utf-8')

        soup = BeautifulSoup(page , 'html.parser')

        lista_produtos = []
    
        produtos = soup.find_all('div', class_=re.compile('productCard'))
        for produto in produtos:
                marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

                lista_produtos.append({'marca': marca, 'preco': preco})
    

        '''
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        produtos = soup.find_all('div', class_=re.compile('productCard'))
        for produto in produtos:
                marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                preco = produto.find('span', class_=re.compile('priceCard')) 
    
                print(marca)
                print(preco)
        
        
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
        driver.quit()

        return jsonify({
            'status': 200,
            'message': 'final da chamada api',
            'data': lista_produtos
        })
    except error as error: 
         print(error)

if __name__ == '__main__':
    app.run( port=5000)