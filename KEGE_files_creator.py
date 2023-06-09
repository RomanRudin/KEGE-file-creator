from os import makedirs, path
from datetime import date
from json import load

name = str(date.today())
name = name[-2:] + '.' + name[-5:-3]
print(name)

if not path.exists(f'{name}'):
    makedirs(f'{name}')

with open('settings.json', 'r', encoding='utf-8')  as file:
    files = load(file)

for file_name, text in files.items():
    with open(f'{name}/{file_name}', 'w') as file:
        if file_name[-3:] == 'txt' or file_name[-3:] == '.py':
            file.write(text)