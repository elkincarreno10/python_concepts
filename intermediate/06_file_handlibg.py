# File Handling

import os

# .txt file
text_file = open('intermediate/my_file.txt', 'w+')
text_file.write('Mi nombre es Elkin\nMi apellido es Carreño\n22 Años\nY mi lenguaje preferido es Python')
# print(text_file.read())
# print(text_file.read(10))
# print(text_file.readline())
# print(text_file.readline())
# print(text_file.readlines())

for line in text_file.readlines():
    print(line)

text_file.write('\nAunque también me gusta javascript')
print(text_file.readline())

text_file.close()

# os.remove('intermediate/my_file.txt')


# .json file

import json

json_file = open('intermediate/my_file.json', 'w+')

json_test = {
    "name": "Elkin",
    "surname": "Carreño",
    "age": 22,
    "languages": ["Pyhton", 'Swift', 'Javascript'],
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open('intermediate/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open('intermediate/my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])

# .csv file

import csv

csv_file = open('intermediate/my_file.csv', 'w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_writer.writerow(['Elkin', 'Carreño', 22, 'Python', 'https://moure.dev'])
csv_writer.writerow(['Roswell', '', 2, 'COBOL', ''])

csv_file.close()

with open('intermediate/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el modulo

# .xml file
import xml
