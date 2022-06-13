import os
import csv


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

reader_files("/home/alpha/Projects/scrape-chicken/data")