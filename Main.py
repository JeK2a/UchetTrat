#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
from filters import *
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

# Просмотр валютных котировок за текущий день
def printKaterovki():
    print("Катеровки валют на текущую дату:")
    print("USD - " + getCursUSD())
    print("EUR - " + getCursEUR())

# Получение списка счетов
def getListChetov(list):
    listChetov = []
    for element in list:
        if listChetov.count(element[4]) == 0:
            listChetov.append(element[4])
    return listChetov




# Просмотр остатков на счетах
def printOstatkov(list):
    listChetov = getListChetov(list)
    listOstatkov = []
    for element in listChetov:
        listOstatkov.append([element, 0])

    i = 0
    while i < len(list):
        j = 0
        while j < len(listChetov):
            if list[i][4] == listChetov[j]:
                if list[i][3] == 1:
                    listOstatkov[j][1] += list[i][2]
                if list[i][3] == 1:
                    listOstatkov[j][1] -= list[i][2]
            j += 1
        i += 1
    for element in listOstatkov:
        print(element)


def printList(list):
    for element in list:
        print(element)


def printListX(list):
    for element in list:
        s = ""
        for t in element:
            s += str(t) + "  "
        print(s)


if __name__ == "__main__":


    printKaterovki()

    list = []

    #list.append(addPozition())
    element = [datetime.now(), "Первая операция", 100, 1, "Основной", "RUB", "Категория 1", "Фактическая"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 0, "Основной", "RUB", "Категория 2", "Планируемая"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 0, "Вторичный", "RUB", "Категория 2", "Планируемая"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 0, "3", "RUB", "Категория 2", "Планируемая"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 1, "Банк", "RUB", "Категория 2", "Планируемая"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 0, "Карта", "RUB", "Категория 2", "Планируемая"]
    list.append(element)

    printList(list)
    # Запись списка в файл
    writeListToFile(list)

    # Получение списка из фала
    list = readFileToList()
    printListX(list)
    print(getListChetov(list))
    printOstatkov(list)
