import os
import csv
from flask import Flask, render_template
from config.index import config
from models.index import create_all_tables
from models.index import Websites, Informations

app = config()[0]
db = config()[1]


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
    return render_template('pages/index.html')





if __name__=='__main__':
    
    create_all_tables()

    app.run(debug = True, port = 5000)