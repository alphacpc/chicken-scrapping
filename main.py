import os
import csv
from flask import Flask, jsonify, render_template
from config.index import config
from models.index import create_all_tables
from models.index import Websites, Informations

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS



# app = config()[0]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/chickens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)


def reader_files(pathname):
    
    tabwebsite = []

    for (root, dirs, file) in os.walk(pathname):
    
        for f in file:

            with open(f'data/{f}', 'r') as fichier:
                i = 0
                reader = csv.reader(fichier)

                for row in reader:
                    if i == 0:
                        pass
                    
                    
                    else:
                        
                        if(row[-1] not in tabwebsite):
                            tabwebsite.append(row[-1])

                            get_website = Websites.query.filter_by(name_website = row[-1]).first()

                            if get_website:
                                pass

                            else:

                                new_website = Websites(name_website = row[-1])
                                
                                db.session.add(new_website)
                                db.session.commit()

                        get_info = Informations.query.filter_by(name_info = row[0]).first()
                        
                        if get_info == None:
                            get_website_id = Websites.query.filter_by(name_website = row[-1]).first().id_website

                            new_info = Informations(
                                name_info = row[0],
                                prix_info = int(row[1]),
                                poids_info = float(row[2]),
                                image_info = row[3],
                                id_website_info = get_website_id
                            )
                            db.session.add(new_info)
                            db.session.commit()
                            print(row)

                    i += 1
                    
    print(tabwebsite)



@app.route('/', methods=["GET"])
def home():
    
    data = Informations.query.all()    

    return render_template('pages/index.html', data = data, websites = Websites)



@app.route('/api/data')
def get_data():
    data = Informations.query.all()
    products = []

    for product in data:

        products.append({
            'nom' : product.name_info,
            'prix' : product.prix_info,
            'poids' : product.poids_info,
            'image' : product.image_info,
            'origine' : Websites.query.get(product.id_website_info).name_website
        })

    return jsonify(products)

@app.route('/api/data/auchan')
def get_data_auchan():
    data = Informations.query.filter_by(id_website_info = 2).all()
    products = []

    for product in data:

        products.append({
            'nom' : product.name_info,
            'prix' : product.prix_info,
            'poids' : product.poids_info,
            'image' : product.image_info,
            'origine' : Websites.query.get(product.id_website_info).name_website
        })

    return jsonify(products)


@app.route('/api/data/baayguins')
def get_data_baayguins():
    data = Informations.query.filter_by(id_website_info = 3).all()
    products = []

    for product in data:

        products.append({
            'nom' : product.name_info,
            'prix' : product.prix_info,
            'poids' : product.poids_info,
            'image' : product.image_info,
            'origine' : Websites.query.get(product.id_website_info).name_website
        })

    return jsonify(products)

@app.route('/api/data/guinarshop')
def get_data_guinarshop():
    data = Informations.query.filter_by(id_website_info = 1).all()
    products = []

    for product in data:

        products.append({
            'nom' : product.name_info,
            'prix' : product.prix_info,
            'poids' : product.poids_info,
            'image' : product.image_info,
            'origine' : Websites.query.get(product.id_website_info).name_website
        })

    return jsonify(products)


if __name__=='__main__':
    
    create_all_tables()

    app.run(debug = True, port = 5000)