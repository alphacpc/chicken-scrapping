from bs4 import BeautifulSoup
import requests
import csv


url = 'https://baayguins.com/product-category/poulets-frais/'
response = requests.get(url)


if response.status_code == 200 :

    soup = BeautifulSoup(response.content, 'html.parser')
    products_list = soup.find('ul', class_="products columns-4")
    products = products_list.find_all('li')



    data = []

    for product in products:
        dict_data = {}

        title = product.find('h2').getText()

        #Traitement sur le prix
        prix = product.find('span', class_='price').find('bdi').getText()
        prix = prix.replace(u'\xa0', u' ')
        prix = prix.split(' ')[0].replace('.','')

        #Traitement sur le poids
        poids = title.split('–')[-1].replace(' ','').replace(',', '.').lower()
        poids = poids.split('kg')[0]

        try:    
            poids = float(poids)
            prix = int(prix)

            dict_data['nom'] = product.find('h2').getText()
            dict_data['prix'] = prix
            dict_data['poids'] = poids
            dict_data['image'] = product.find('img', class_='attachment-woocommerce_thumbnail').get('src')
            dict_data['site'] =  'baayguins.com'


            data.append(dict_data)

        except ValueError:
            
            pass

    #Ecriture du fichier csv
    with open('../data/data-baaygins.csv', "w") as file:

        donne = csv.DictWriter(file, list(data[0].keys()))
        donne.writeheader()
        donne.writerows(data)


else:

    print("Url incorrect !")


