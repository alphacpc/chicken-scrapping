from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from config import email, password
import csv

#Déclaration des variables
data = []

###Ouvrir le navigateur
driver = webdriver.Chrome()
driver.get("https://compte.auchan.fr/auth/realms/auchan.fr/protocol/openid-connect/auth?client_id=lark-crest&state=768aa303-8d84-4389-97ff-88f3518aa674&redirect_uri=https%3A%2F%2Fwww.auchan.fr%2Fauth%2Flogin%2F68747470733a2f2f7777772e61756368616e2e66722f626f756368657269652d766f6c61696c6c652d706f6973736f6e6e657269652f766f6c61696c6c652d6c6170696e2f706f756c65742f706f756c6574732d656e74696572732f63612d6e3032303230313031%3Fauth_callback%3D1&scope=openid&response_type=code")

###Pour se logger
driver.find_element_by_name('username').send_keys(email)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div[1]/button').click()

#Stopper le programme pendant 1s
sleep(1)

#
# driver.get("https://www.auchan.fr")
driver.get("https://www.auchan.fr/boucherie-volaille-poissonnerie/volaille-lapin/poulet/poulets-entiers/ca-n02020101")

#Stopper le programme pendant 2s
sleep(2)

#Utilisation de BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')


for product in soup.find_all('article', class_="list__item"):

    try:

        dict_data = {}

        prix = product.find('div', class_='product-price bolder text-dark-color').getText()
        prix = prix.split('€')[0].replace(',', '.')
        prix = float(prix) * 642.33 # Le 13juin 2022 1£ => 642.33 FCFA (google)


        dict_data['nom'] = product.find('p', class_="product-thumbnail__description").getText().replace('\n','')
        dict_data['prix'] = round(prix)
        dict_data['poids'] = product.find("div", class_="product-thumbnail__attributes").find('span').getText()
        dict_data['image'] = product.find('source').get('srcset').split(' ')[0]
        dict_data['site'] =  'auchan.fr'

        data.append(dict_data)

    except:
        pass

#Permet le Navigateur apres récupération des données
driver.close()


with open('../data/data-auchan.csv', "w") as file:

    donne = csv.DictWriter(file, list(data[0].keys()))
    donne.writeheader()
    donne.writerows(data)