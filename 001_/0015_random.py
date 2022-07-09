# import random

# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)

# print(num1)
# print(num2)

# import random


# for _ in range(10):
#     print(random.randint(1, 100))

# import random

# num = random.randrange(10)

# import random

# num = random.randrange(5, 10)

# import random

# num = random.randrange(0, 101, 10)

# import random

# num = random.random()
# print(num)

# import random

# num = random.uniform(1.5, 17.3)
# print(num)

# import random

# # явно устанавливаем начальное значение для генератора случайных чисел
# random.seed(17)

# for _ in range(10):
#     print(random.randint(1, 100))
####
#from random import *
# Return random integer in range [a, b], including both end points.
# def randint(self, a, b):
#     return self.randrange(a, b + 1)
####

# import random

# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# import random

# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')

# import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)

# import random

# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(['a', 'b', 'c', 'd']))

# import random

# numbers = [2, 5, 8, 9, 12]

# print(random.sample("numbers", 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, 3))
# print(random.sample(numbers, 5))

# import random

# numbers = list(range(2, 10, 2)) + [3]
# print(numbers)

# num = random.choice(numbers)
# print(num)

# import random

# numbers = [1, 2, 4, 6, 7, 9]

# rand_numbers = random.sample(numbers, 3)

# print(rand_numbers)

# import math

# n = int(input())

# x = math.ceil(math.log2(n))

# print(x)

# import random

# from matplotlib import use

# x = random.randint(1, 100)
# print('Добро пожаловать в числовую угадайку')


# def is_valid(n):
#     if 1 <= n <= 100:
#         return True
#     else:
#         return False


# user_quess = -1

# while True:
#     user_quess = int(input())
#     if not is_valid(user_quess):
#         print('А может быть все-таки введем целое число от 1 до 100?')
#     elif user_quess < x:
#         print('Ваше число меньше загаданного, попробуйте еще разок')
#     elif user_quess > x:
#         print('Ваше число больше загаданного, попробуйте еще разок')
#     else:
#         print('Вы угадали, поздравляем')
#         break

# Шифр цезаря
# Задаем четыре вопроса пользователю: шифр-дешифр, язык, шаг, текст.
# За каждым вопросом стоит while-проверка, что введенный ответ является корректным значением.

# whats_direction = input(
#     'Что мы должны сделать: шифровать или дешифровать? \n').lower()
# while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
#     whats_direction = input(
#         'Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n').lower()


# whats_language = input('Какой нужен язык: русский или английский? \n').lower()
# while whats_language != 'русский' and whats_language != 'английский':
#     whats_language = input(
#         'Что-то не то ты ввёл. Напиши "русский" либо "английский". \n').lower()


# whats_step = input(
#     'На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
# while whats_step.isdigit() != True:
#     whats_step = input('Что-то не то ты ввёл. Напиши число. \n')


# whats_text = input('Какой текст нужно использовать сейчас? \n')
# while whats_text.isspace() == True:
#     whats_text = input('Что-то не то ты ввёл. Введи текст. \n')


# Объявляем функцию с четырьмя аргументами – соответственно четырем вопросам.
# def caesar(direction, language, step, text):

#     # Четыре словаря под русские и английские символы, большие и маленькие.
#     # В теории можно обойтись без них и обращаться к таблице Unicode.
#     # Но мне было удобнее создать свои словари.

#     upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

#     # Объявляем цикл for. Количество итераций равно длине строки text.
#     for i in range(len(text)):

#         # Задаем локальные переменные: длину алфавита и значения словарей.
#         if language == 'русский':
#             alphas = 32
#             low_alphabet = lower_rus_alphabet
#             upp_alphabet = upper_rus_alphabet
#         if language == 'английский':
#             alphas = 26
#             low_alphabet = lower_eng_alphabet
#             upp_alphabet = upper_eng_alphabet

#         # Если text[i] является буквой:
#         if text[i].isalpha():

#             # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
#             if text[i] == text[i].lower():
#                 place = low_alphabet.index(text[i])
#             if text[i] == text[i].upper():
#                 place = upp_alphabet.index(text[i])

#             # Если нужно дешифровать, то:
#             if direction == 'дешифровать':
#                 # Находим индекс для измененного символа.
#                 # Новый ндекс = Старый индекс - Шаг % Длина алфавита
#                 index = (place - int(step)) % alphas

#             # Если нужно зашифровать, то:
#             elif direction == 'шифровать':
#                 # Находим индекс для измененного символа.
#                 # Новый ндекс = Старый индекс + Шаг % Длина алфавита
#                 index = (place + int(step)) % alphas

#             # Выводим измененный символ.
#             if text[i] == text[i].lower():
#                 print(low_alphabet[index], end='')
#             if text[i] == text[i].upper():
#                 print(upp_alphabet[index], end='')

#         # Если text[i] не является буквой:
#         else:
#             # Делаем print этого символа без изменений.
#             print(text[i], end='')


# Вызываем функцию, передавая в аргументы четыре input`а из начала кода.
# caesar(whats_direction, whats_language, whats_step, whats_text)
###########################################

# for i in range(26):
#     caesar("дешифровать", "английский",
#            i, "Hawnj pk swhg xabkna ukq nqj.")
#     print()

##########################################################################
##########################################################################
##########################################################################
# def caesar(direction, language, step, text):

#     # Четыре словаря под русские и английские символы, большие и маленькие.
#     # В теории можно обойтись без них и обращаться к таблице Unicode.
#     # Но мне было удобнее создать свои словари.

#     upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

#     # Объявляем цикл for. Количество итераций равно длине строки text.
#     new_str = ''
#     for i in range(len(text)):

#         # Задаем локальные переменные: длину алфавита и значения словарей.
#         if language == 'русский':
#             alphas = 32
#             low_alphabet = lower_rus_alphabet
#             upp_alphabet = upper_rus_alphabet
#         if language == 'английский':
#             alphas = 26
#             low_alphabet = lower_eng_alphabet
#             upp_alphabet = upper_eng_alphabet

#         # Если text[i] является буквой:
#         if text[i].isalpha():

#             # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
#             if text[i] == text[i].lower():
#                 place = low_alphabet.index(text[i])
#             if text[i] == text[i].upper():
#                 place = upp_alphabet.index(text[i])

#             # Если нужно дешифровать, то:
#             if direction == 'дешифровать':
#                 # Находим индекс для измененного символа.
#                 # Новый ндекс = Старый индекс - Шаг % Длина алфавита
#                 index = (place - int(step)) % alphas

#             # Если нужно зашифровать, то:
#             elif direction == 'шифровать':
#                 # Находим индекс для измененного символа.
#                 # Новый ндекс = Старый индекс + Шаг % Длина алфавита
#                 index = (place + int(step)) % alphas

#             # Выводим измененный символ.
#             if text[i] == text[i].lower():
#                 new_str += low_alphabet[index]

#             if text[i] == text[i].upper():
#                 new_str += upp_alphabet[index]

#         # Если text[i] не является буквой:
#         else:
#             # Делаем print этого символа без изменений.
#             new_str += text[i]

#     return new_str


# sentence = input().split(' ')
# new_sentense = ''
# for i in range(len(sentence)):
#     word_len = 0
#     if '.' in sentence[i] or ',' in sentence[i] or '!' in sentence[i] or '?' in sentence[i]:
#         word_len = len(sentence[i])-1
#     elif '\"' in sentence[i] or "\'" in sentence[i]:
#         word_len = len(sentence[i])-2
#     else:
#         word_len = len(sentence[i])

#     new_word = caesar("шифровать", "английский", word_len, sentence[i])
#     new_sentense += new_word + " "
# print(new_sentense)
##########################################################################
##########################################################################
##########################################################################

# print(int("11001", 2))
#####
# base = 9
# while True:
#     if (int("88", base) == (int("32", base)+int("22", base)+int("16", base)+int("17", base))):
#         break
#     else:
#         base += 1
# print(base)

#################
# digit = input('Введите число: ')

# sys = int(input('Введите основание системы счисления: '))


# def from_ten(digit, sys):
#     digit = int(digit)
#     sp = []
#     while digit > 0:
#         a = int(digit % sys)
#         if a > 9:
#             a = chr(a + 55)
#         sp.append(a)
#         digit //= sys
#     sp.reverse()

#     for i in sp:
#         print(i, end='')


# from_ten(digit, sys)
###########################################
# print(bin(10))
# print(bin(128))
# print(bin(150))
# print(bin(18765))
###########################################
# print(oct(10))
# print(oct(128))
# print(oct(150))
# print(oct(18765))
##########################################
# print(hex(10))
# print(hex(128))
# print(hex(150))
# print(hex(18765))
##########################################
# num = 127
# bin_num = bin(num)  # 0b1111111
# oct_num = oct(num)  # 0o177
# hex_num = hex(num)  # 0x7f

# print(bin_num[2:])  # 1111111
# print(oct_num[2:])  # 177
# print(hex_num[2:])  # 7f
##########################################
# num = 127432

# hex_num = hex(num)          # 0x1f1c8
# print(hex_num[2:].upper())  # 1F1C8
##########################################
# num = int(input())
# bin_num = bin(num)
# oct_num = oct(num)
# hex_num = hex(num)

# print(bin_num[2:])
# print(oct_num[2:])
# print(hex_num[2:].upper())
