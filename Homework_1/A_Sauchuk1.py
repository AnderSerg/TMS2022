"""Homework for thursday 31.03.2022"""

# TODO: Задания для самостоятельной работы
#  1. Создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами
#  2. Создать 2 перменных с одинаковыми данными с разными идентификаторами
#  3. Поменять их типы так, чтобы у 1х трех были разные идентификаторы, а у 2х последних были одинаковые

#   1. Создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами
variable1 = variable2 = variable3 = 500
print('1 Проверка одинаковые ли данные:', variable1 == variable2 == variable3)
print('1 Вывод идентификаторов:', id(variable1), id(variable2), id(variable3), '\n')

#   2. Создать 2 перменных с одинаковыми данными с разными идентификаторами
string1 = str(1)
string2 = str(1)
print('2 Проверка одинаковые ли данные:', string1 == string2)
print('2 Вывод идентификаторов:', id(string1), id(string2), '\n')

#   3. Поменять их типы так, чтобы у 1х трех были разные идентификаторы, а у 2х последних были одинаковые
var1 = str(variable1)
var2 = str(variable2)
var3 = str(variable3)
print('3.1 Проверка одинаковые ли данные:', var1 == var2 == var3)
print('3.1 Вывод идентификаторов:', id(var1), id(var2), id(var3), '\n')

string1_3 = int(string1)
string2_3 = int(string2)
print('3.2 Проверка одинаковые ли данные:', string1_3 == string2_3)
print('3.2 Вывод идентификаторов:', id(string1_3), id(string2_3))
