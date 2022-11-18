#!/bin/bash
# !/usr/bin/python3

import json


def transform_to_csv(data_def):
    # /home/anatol/Документы/GitHub/HometasksTMS/Lesson_8/Task_5.csv
    name_file = input("Укажите имя файла без расширения: ") + ".csv"
    if name_file == ".csv":
        print("Имя файла не было указано, будет использовано имя по умолчанию: 'Task_5.csv'")
        name_file = 'Task_5.csv'
    with open(name_file, 'w') as file_def:
        for i in data_def:
            file_def.write(str(data_def[i]['Name']) + ',')
            file_def.write(str(data_def[i]['Age']) + ',')
            file_def.write(str(i) + '\n')


#  Задание понял так, что файл открывается вне функции, а потом применяется фукция для трансформации
try:
    path_JSON = input("Укажите путь к файлу JSON (!!!файл и расширение не указывать!!!): ") + 'Task_4.json'
    with open(path_JSON) as file:
        data = json.load(file)

except FileNotFoundError:
    print("Путь к файлу был указанневерно, будет использован путь по умолчанию")
    path_JSON = '/home/anatol/Документы/GitHub/HometasksTMS/Lesson_8/Task_4.json'
    with open(path_JSON) as file:
        data = json.load(file)

transform_to_csv(data)
