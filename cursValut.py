#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from xml.etree import ElementTree as ET


# Получение курса доллара
def getCursUSD():
    valuta = ET.parse(urllib.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))

    for line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == "R01235":
            return line.find('Value').text


# Получение курса евро
def getCursEUR():
    valuta = ET.parse(urllib.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))

    for line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == "R01239":
            return line.find('Value').text


if __name__ == "__main__":
    print getCursUSD()
    print getCursEUR()
