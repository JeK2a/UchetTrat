#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
from cursValut import getCursUSD, getCursEUR

VALUTS = ["RUB", "USD", "EUR"]


# Запись списка в файл
def writeListToFile(list, fileName="list.txt"):
    f = open(fileName, "w")
    for element in list:
        s = ""
        for e in element:
            s = s + str(e) + "|"
        f.writelines(str(s) + "\n")
    f.close()
    pass


# Получение списка из фала
def readFileToList(fileName="list.txt"):
    f = open(fileName, "r")
    listIn = f.readlines()
    f.close()
    listOut = []
    for element in listIn:
        element = element.split("|")
        timedate = datetime.strptime(element[0][:19], "%Y-%m-%d %H:%M:%S")
        listOut.append([timedate, element[1], int(element[2]), int(element[3]),
                        element[4], element[5], element[6], element[7]])
    return listOut


# Добавление новой позиции в список
def addPozition():
    now = datetime.now()
    name = str(input("Введите имя операции: "))
    summa = int(input("Ведите сумму расхода/дохода: "))
    dohodRashod = int(input("Введите 1 если доход / 0 если расход: "))
    chet = input("Введите название счета: ")
    valuta = input("Введите название валюты: ")
    kategory = input("Введите название категории: ")
    faktPlan = input("Фактическая или планируемая операция: ")
    return [now, name, summa, dohodRashod, chet, valuta, kategory, faktPlan]


# Фильтр по дате позиций
def filterDate(listIn, dataStart=None, dataEnd=None):
    listOut = []
    if dataStart is None and dataEnd is None:
        print("Необходимо указать минимум одну дату отбора")
        return None
    if dataStart is None:
        for element in listIn:
            if element[0] <= dataEnd:
                listOut.append(element)
    if dataEnd is None:
        for element in listIn:
            if element[0] >= dataStart:
                listOut.append(element)
    if dataStart is not None and dataEnd is not None:
        for element in listIn:
            if dataStart <= element[0] <= dataEnd:
                listOut.append(element)
    return listOut


# Фильтр доход/расход
def filterDohodRashod(listIn, dohodRashod=None):
    listOut = []
    if dohodRashod != 1 or dohodRashod != 0:
        print("Необходимо указать название счета")
        return None
    for element in listIn:
        if element[4] == dohodRashod:
            listOut.append(element)
    return listOut


# Фильтр по названию счета
def filterChet(listIn, cher=""):
    listOut = []
    if cher == "":
        print("Необходимо указать название счета")
        return None
    else:
        for element in listIn:
            if element[4] == cher:
                listOut.append(element)
        return listOut


# Фильтр по категории счета
def filterKategory(listIn, kategory=""):
    listOut = []
    if kategory == "":
        print("Необходимо указать название категории")
        return None
    else:
        for element in listIn:
            if element[6] == kategory:
                listOut.append(element)
        return listOut


# Обмен валю
def obmenVavut(self, valuta=None):
    if valuta == None:
        print("Не указана валюта, на которую необходимо обменять")
        return None
    if self[5] == valuta:
        print("Выберите валюту, отличную от текущей")
        return None
    if self[5] == "RUB":
        if valuta == "USD":
            self[2] /= getCursUSD()
        if valuta == "EUR":
            self[2] /= getCursEUR()
    if self[5] == "USD":
        self[2] *= getCursUSD()
        if valuta == "EUR":
            self[2] /= getCursEUR()
    if self[5] == "EUR":
        self[2] *= getCursEUR()
        if valuta == "USD":
            self[2] /= getCursUSD()
    return self


if __name__ == "__main__":
    print(getCursUSD())
    print(getCursEUR())

    list = []

    # list.append(addPozition())
    element = [datetime.now(), "Первая операция", 100, 1, "Основной", "RUB", "Категория 1", "Фактическая"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 0, "Основной", "RUB", "Категория 2", "Планируемая"]
    list.append(element)

    print(list)
    # Запись списка в файл
    writeListToFile(list)

    # Получение списка из фала
    list = readFileToList()
    print(list)
