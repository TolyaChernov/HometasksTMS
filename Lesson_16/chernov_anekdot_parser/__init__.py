"""Скрипт выводит один случаайный анекдот с сайта "anekdot.ru\""""
import requests  # pip install requests
from bs4 import BeautifulSoup as soup  # pip install beautifulsoup4
import random


def anekdot():
    """Функция для парсинга и вывода случайного анекдота"""
    url = "https://www.anekdot.ru/last/anekdot/"  # Допускается заменить страницу
    r = requests.get(url)
    html = soup(r.content, "html.parser")

    buff = html.find_all("div", class_="text")
    anekdots_list = []
    for i in buff:
        anekdots_list.append(
            i.get_text(strip=True, separator=" ")
        )  # Создаем список анекдотов
    random.shuffle(anekdots_list)  # Перемешиваем список
    return anekdots_list[0]  # Вывод первого анекдота из измененного списка
    print(anekdot())


print(anekdot())
