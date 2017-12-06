#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
from cursValut import getCursUSD, getCursEUR


def writeListToFile(list):
    f = open("1.txt", "w")
    for element in list:
        now, name, summa, dohodRashod = element
        f.writelines(str(now) + "|" + name + "|" + str(summa) + "|" + str(dohodRashod) + "\n")
    f.close()
    pass


def readFileToList():
    f = open("1.txt", "r")
    listIn = f.readlines()
    f.close()
    listOut = []
    for element in listIn:
        element = element.split("|")
        timedate = datetime.strptime(element[0][:19], "%Y-%m-%d %H:%M:%S")
        listOut.append([timedate, element[1], int(element[2]), int(element[3])])
    return listOut


if __name__ == "__main__":


    print(getCursUSD())
    print(getCursEUR())


    #  now = datetime.now()
    #  name = str(input("Введите имя операции:"))
    #  summa = int(input("Ведите сумму расхода/дохода: "))
    #  dohodRashod = int(input("ВВедите 1 если доход / 0 если расход :"))
    #  if dohodRashod == 0:
    #      summa *= -1

    list = []
    oper = [datetime.now(), "Первая операция", 100, 1]
    list.append(oper)
    oper = [datetime.now(), "Вторая операция", -200, 0]
    list.append(oper)
    print(list)
    writeListToFile(list)
    list = readFileToList()
    print(list)



