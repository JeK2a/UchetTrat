#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *

from cursValut import getCursUSD, getCursEUR


if __name__ == "__main__":
    print "USD - ", getCursUSD()
    print "EUR - ", getCursEUR()

    operations = []
    name = ""

    now = datetime.now()
    name = input("Введите название расхода/дохода: ")
    summa = int(input("Ведите сумму расхода/дохода: "))
    dohodRashod = bool(input("ВВедите 1 если доход / 0 если расход :"))

    oper = (now, name, summa, dohodRashod)
    print oper

    operations.append(oper)
    print(operations)
