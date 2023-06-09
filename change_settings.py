from os import makedirs, path, listdir
from datetime import date
from json import dump

if path.exists('SETTINGS'):
    data = {}
    for file_name in listdir('SETTINGS'):
        with open(f'SETTINGS/{file_name}', 'r') as file:
            if file_name[-3:] == 'txt' or file_name[-3:] == '.py':
                data[file_name] = file.read()
            else:
                data[file_name] = ''

    print(data)
    with open('settings.json', 'w', encoding='utf-8')  as file:
        dump(data, file, indent=4, sort_keys=False, ensure_ascii=False)