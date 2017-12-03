from datetime import datetime


class Oper:
    date = datetime.now()
    name = ""
    chet = ""
    valuta = ""

    def __init__(self, date, name, chet, valuta):
        self.date = date
        self.name = name
        self.chet = chet
        self.valuta = valuta



