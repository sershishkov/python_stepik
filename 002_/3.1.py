# num1 = 3 * True - (True + False)
# num2 = (True + True + False) ** 3 + 5
# print(num1 + num2)
######################################################
# a = 6
# b = 10
# print(not a == 10 and b == 10)
######################################################
# a = 6
# b = 10
# print(not(not a == 10 or not b == 10))
######################################################
# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)
######################################################
# print(isinstance(3, int))
# print(isinstance(3.5, float))
# print(isinstance('Beegeek', str))
# print(isinstance([1, 2, 3], list))
# print(isinstance(True, bool))
######################################################
# print(type(3))
# print(type(3.5))
# print(type('Beegeek'))
# print(type([1, 2, 3]))
# print(type(True))
######################################################


# 15 #########################
# Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2 и возвращающую значение True если число num1 делится без остатка на число num2 и False в противном случае.
# объявление функции


def func(num1, num2):
    return num1 % num2 == 0


# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print("делится")
else:
    print("не делится")

######################################################
