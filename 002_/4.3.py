######################################################

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = []

# for _ in range(n):
#     my_list.append([0] * m)

# print(my_list)
######################################################
######################################################

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n

# for i in range(n):
#     my_list[i] = [0] * m

# print(my_list)
######################################################
######################################################
# n, m = int(input()), int(input())    # считываем значения n и m

# my_list = [[0] * m for _ in range(n)]

# print(my_list)
######################################################
######################################################
# n = 4                                          # количество строк (элементов)
# my_list = []

# for _ in range(n):
#     # создаем список из элементов строки
#     elem = [int(item) for item in input().split()]
#     my_list.append(elem)
# print(my_list)
######################################################
######################################################
# n = 4
# my_list = []

# for _ in range(n):
#     elem = [int(i) for i in input().split()]
#     my_list.extend(elem)
# print(my_list)
######################################################
######################################################
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(my_list[0][0])
# print(my_list[1][2])
# print(my_list[2][1])
######################################################
######################################################
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         # используем необязательный параметр end
#         print(my_list[i][j], end=' ')
#     print()
######################################################
######################################################
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()
######################################################
######################################################
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         # выводим my_list[j][i] вместо my_list[i][j]
#         print(my_list[j][i], end=' ')
#     print()
######################################################
######################################################
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         total += my_list[i][j]
# print(total)
######################################################
######################################################
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

# total = 0
# for row in my_list:
#     for elem in row:
#         total += elem
# print(total)
######################################################
######################################################
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

# total = 0
# for row in my_list:      # в один цикл
#     total += sum(row)
# print(total)
######################################################
######################################################

######################################################
# list1 = [[1, 2, 3], [4, 5]]
# list2 = list1

# list1[0].append(7)

# print(list2)
######################################################
# list1 = [[1] * 3] * 3
# list1[0][1] = 5
# print(list1[1][1])
# print(list1)
######################################################
# n = 3
# list1 = []

# for _ in range(n):
#     row = input().split()
#     list1.extend(row)

# print(list1)
######################################################
# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

# maximum = my_list[0][0]
# minimum = my_list[0][0]

# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)

# print(maximum + minimum)
######################################################
# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

# maximum = my_list[0][0]
# minimum = my_list[0][0]

# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)

# print(maximum + minimum)

# 8 #########################
# На вход программе подается число nn. Напишите программу, которая создает и выводит построчно список, состоящий из nn списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
# n = int(input())
# list_1 = [i+1 for i in range(n)]
# for _ in range(n):
#     print(list_1)

######################################################

# 9 #########################
# На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список, состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
# n = int(input())
# for i in range(n):
#     list_1 = [i+1 for i in range(i+1)]
#     print(list_1)

######################################################

# 10 #########################
# Треугольник Паскаля 1 🌶️
# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).
# import math


# def pascal(row_number):
#     my_list = []
#     if row_number == 0:
#         my_list = [1]
#     elif row_number == 1:
#         my_list = [1, 1]
#     elif row_number == 2:
#         my_list = [1, 2, 1]
#     else:
#         my_list.append(1)
#         for i in range(1, row_number):
#             new_item = round(math.factorial(
#                 row_number) / (math.factorial(i)*math.factorial(row_number - i)))
#             my_list.append(new_item)
#         my_list.append(1)

#     return my_list


# row_number = int(input())
# print(pascal(row_number))


######################################################

# 11 #########################
# На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.
# import math


# def pascal(row_number):
#     my_list = []
#     if row_number == 0:
#         my_list = [1]
#     elif row_number == 1:
#         my_list = [1, 1]
#     elif row_number == 2:
#         my_list = [1, 2, 1]
#     else:
#         my_list.append(1)
#         for i in range(1, row_number):
#             new_item = round(math.factorial(
#                 row_number) / (math.factorial(i)*math.factorial(row_number - i)))
#             my_list.append(new_item)
#         my_list.append(1)

#     return my_list


# row_number = int(input())
# for i in range(row_number):
#     print(*pascal(i))

######################################################

# 12 #########################
# Упаковка дубликатов 🌶️
# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.
# def pack_sentence(sentence):
#     sentence_list = sentence.split()
#     new_list = []
#     j = 0
#     new_list.append([sentence_list[0]])
#     for i in range(1, len(sentence_list)):
#         if sentence_list[i] == sentence_list[i-1]:
#             new_list[j].append(sentence_list[i])
#         else:
#             j += 1
#             new_list.append([sentence_list[i]])

#     return new_list


# sentence = input()
# print(pack_sentence(sentence))

######################################################

# 13 #########################
# Разбиение на чанки 🌶️
# На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка(куска), а возвращает список из чанков указанной длины.

def chunked(sentence, chunk_length):
    sentence = sentence.split()
    new_list = []
    j = 0
    for i in range(0, len(sentence), chunk_length):
        new_list.append([sentence[i]])
        new_list[j].extend(sentence[i+1:i+chunk_length])
        j += 1

    return new_list


# sentence = input()
# chunk_length = int(input())
# print(chunked(sentence, chunk_length))
######################################################

# 14 #########################
# Подсписки списка 🌶️🌶️
# Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

# На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

start_list = input().split()
new_list = []
new_list.append([])
for i in range(len(start_list)):
    inner_list = []
    for j in range(len(start_list)):
        if len(start_list[j:j+i+1]) == i + 1:
            inner_list.append(start_list[j:j+i+1])
    new_list.extend(inner_list)

print(new_list)


######################################################
