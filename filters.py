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