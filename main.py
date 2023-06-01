from typing import Final

import input
import datetime
import interpolation as interpol  # xD

from interpolation import get_finite_differences_table

# dots = [[2.1, 3.759], [2.15, 4.186], [2.2, 4.922], [2.25, 5.349], [2.3, 5.928], [2.35, 6.419], [2.4, 7.084]]
# table = get_finite_differences_table(dots)
# print(table)

def print_table(table):
    for node in table:
        print(node + " ")


FILENAME: Final[str] = 'test.txt'

print('Вас приветствует программа "интерполяция функции"! Текущее время: ' + str(datetime.datetime.now()))
print('Выберите тип ввода функции: ')
print('1. Файл')
print('2. Клавиатура')
print('3. Список функций')

input_type = int(input())
match input_type:
    case 1:
        print('Выбранный тип ввода: файл')
        table = input.get_table_from_file(FILENAME)
        print_table(table)