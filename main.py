import os
import csv
from flask import Flask, render_template
from config.index import app
from models.index import create_all_tables


app = Flask(__name__)

def reader_files(pathname):
    for (root, dirs, file) in os.walk(pathname):
    
        for f in file:

            with open(f'data/{f}', 'r') as fichier:
                i = 0
                reader = csv.reader(fichier)

                for row in reader:
                    if i == 0:
                        pass
                    
                    else:

                        print(row)

                    i += 1

# reader_files("./data")


@app.route('/', methods=["GET"])
def home():
    return render_template('pages/index.html')





if __name__=='__main__':
    
    create_all_tables()

    app.run(debug = True, port = 5000)