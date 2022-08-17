import pandas
from datetime import datetime
import os

class Row:
    def __repr__(self):
        return f"{self.name}"

    def __init__(self, instruments=[], name):
        self.instruments = instruments
        self.name = name

    def get_instruments():
        pass

    def get_get_cost():
        pass

    def get_due_date(current_date):
        pass

    def get_name():
        pass
        name = input('Type in your name: ')
        return name

    def get_phone_num():
        pass
        num = ['Type in your phone number with no spaces or dashes: ']
        return num

current_date = datetime.now().strftime("%D")

def clear():
    os.system('clear')


def get_input(current_date):
    pass
    list_of_rows = []
    while True:
        row = []
        name = get_name()
        phone_number = get_phone_num()
        instruments = get_instruments()
        cost = get_cost(instruments)
        due_date = get_due_date(current_date)
        row.append(name, phone_number, instruments, cost, due_date)
        list_of_rows.append(row)
    return list_of_rows

data = []
for row in get_input():
    data.append(row)

registry = pandas.DataFrame(data)
print(registry)
