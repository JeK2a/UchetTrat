#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
from cursValut import getCursUSD, getCursEUR


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
        listOut.append([timedate, element[1], int(element[2]), int(element[3]), element[4], element[5]])
    return listOut


def addPozition():
    now = datetime.now()
    name = str(input("Введите имя операции:"))
    summa = int(input("Ведите сумму расхода/дохода: "))
    dohodRashod = int(input("ВВедите 1 если доход / 0 если расход :"))
    chet = input("Введите название счета: ")
    valuta = input("Введите название валюты: ")
    return [now, name, summa, dohodRashod, chet, valuta]


def filterDohodRashod(listIn, dohodRashod):
    listOut = []
    for element in listIn:
        if element[4] == dohodRashod:
            listOut.append(element)
    return listOut


def filterData(listIn, dataStart = None, dataEnd = None):
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


if __name__ == "__main__":
    print(getCursUSD())
    print(getCursEUR())

    list = []

    # list.append(addPozition())
    element = [datetime.now(), "Первая операция", 100, 1, "Основной", "RUB"]
    list.append(element)
    element = [datetime.now(), "Вторая операция", 200, 0, "Основной", "RUB"]
    list.append(element)

    print(list)
    # Запись списка в файл
    writeListToFile(list)

    # Получение списка из фала
    list = readFileToList()
    print(list)
