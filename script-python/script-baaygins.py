from bs4 import BeautifulSoup
from pprint import pprint

import requests
import csv

url = 'https://baayguins.com/product-category/poulets-frais/'
response = requests.get(url)
print(response.status_code)

if response.status_code == 200 :

    soup = BeautifulSoup(response.content, 'html.parser')
    products_list = soup.find('ul', class_="products columns-4")
    products = products_list.find_all('li')



    data = []

    for product in products:
        dict_data = {}

        title = product.find('h2').getText()
        prix = product.find('span', class_='price').find('bdi').getText()

        print(prix)
        print(prix.split('x'))

        dict_data['nom'] = title
        dict_data['prix'] = prix.replace(u'\xa0', u' ')
        dict_data['poids'] = title.split('–')[-1]
        dict_data['image'] = product.find('img', class_='attachment-woocommerce_thumbnail').get('src')
        dict_data['site'] =  'baayguins.com'

        pprint(dict_data)

        data.append(dict_data)

else:

    print("Adresse Url incorrect !")



with open('../data/data-baaygins.csv', "w") as file:

    donne = csv.DictWriter(file, list(data[0].keys()))
    donne.writeheader()
    donne.writerows(data)