# # объявление функции
# def draw_box():
#     for i in range(14):
#         if i == 0 or i == 13:
#             print("*"*10)
#         else:
#             print("*"+" "*8 + "*")
# # основная программа
# draw_box()  # вызов функции

# def draw_triangle():
#     for i in range(1, 11):
#         print("*"*i)
# # основная программа
# draw_triangle()  # вызов функции

# def draw_box(height, width):    # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)


# draw_box(10, 15)


# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)


# print_number(2, 3, 11)


# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)


# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1


# print_text('Python', 4)


# def draw_triangle(fill, base):
#     middle = base//2+1
#     for i in range(1, base+1):
#         if i <= middle:
#             print(fill*i)
#         else:
#             print(fill*(base-i+1))


# # считываем данные
# fill = input()
# base = int(input())

# # вызываем функцию
# draw_triangle(fill, base)

# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper() + name[0].upper()+patronymic[0].upper())


# # считываем данные
# name, surname, patronymic = input(), input(), input()

# # вызываем функцию
# print_fio(name, surname, patronymic)

# # объявление функции
# def print_digit_sum(num):
#     my_list = [int(item) for item in list(str(num))]
#     print(sum(my_list))


# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)


# def swap(a, b):
#     a, b = b, a


# a = 4
# b = 3
# swap(a, b)
# print(a - b)

# x = 5


# def add():
#     global x
#     x = 3
#     x = x + 5
#     print(x)


# add()
# print(x)


# # функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result


# # основная программа
# temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия


# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     return result


# print(do_something([2, 2, 2, 2]))


# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)


# print(get_sum(1, 2, 3))

# def convert_to_miles(km):
#     return km * 0.6214


# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))

# def get_days(month):
#     if month == 2:
#         return 28
#     elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         return 31
#     else:
#         return 30


# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))


# # объявление функции
# def get_factors(num):
#     my_list = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             my_list.append(i)
#     return my_list


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))

# def number_of_factors(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#     return count


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_of_factors(n))

# объявление функции


# def find_all(target, symbol):
#     indexes_list = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             indexes_list.append(i)

#     return indexes_list


# # считываем данные
# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))

# # print(find_all('abcdabcaaa', 'a'))
# # print(find_all('abcadbcaaa', 'e'))
# # print(find_all('abcadbcaaa', 'd'))


# def merge(list1, list2):
#     new_list = list1 + list2
#     new_list.sort()
#     return new_list


# # # считываем данные
# # numbers1 = [int(c) for c in input().split()]
# # numbers2 = [int(c) for c in input().split()]

# # # вызываем функцию
# # print(merge(numbers1, numbers2))

# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))


# def quick_merge(list1, list2):
#     result = []

#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2

#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1

#     if p1 < len(list1):   # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]

#     return result


# n = int(input())
# list_result = []
# for i in range(n):
#     new_list = [int(i) for i in input().split(" ")]
#     list_result = quick_merge(list_result, new_list)

# print(*list_result)

# def is_invalid(model):
#     if model != 100 and model != 200 and model != 300:
#         return True
#     else:
#         return False


# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side2 > side1:
#         return True
#     else:
#         return False


# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# # объявление функции
# def is_prime(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))

# # объявление функции
# def is_prime(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False


# def get_next_prime(num):

#     top_number = num+1
#     while not is_prime(top_number):
#         top_number += 1
#     return top_number


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))


# def is_password_good(password):
#     is_good = True
#     if len(password) >= 8:
#         is_good = True
#     else:
#         is_good = False

#     if password.upper() != password and is_good:
#         is_good = True
#     else:
#         is_good = False

#     if password.lower() != password and is_good:
#         is_good = True
#     else:
#         is_good = False

#     has_digit = False
#     for i in range(len(password)):
#         if password[i].isnumeric():
#             has_digit = True
#             break

#     return has_digit and is_good


# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))


# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     else:
#         count = 0
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 count += 1
#         if count == 1:
#             return True
#         else:
#             return False


# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))

# def is_palindrome(text):
#     my_list = []
#     for i in range(len(text)):
#         if text[i] != " " and text[i] != "," and text[i] != "." and text[i] != "!" and text[i] != "?" and text[i] != "-":
#             my_list.append(text[i].lower())

#     new_str = ''.join(my_list)

#     return new_str == new_str[::-1]


# # # считываем данные
# # txt = input()

# # # вызываем функцию
# # print(is_palindrome(txt))

# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))

# def is_prime(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False


# def is_valid_password(password):
#     my_list = password.split(":")
#     is_good = True
#     if len(my_list) != 3 or not my_list[0].isnumeric() or not my_list[1].isnumeric() or not my_list[2].isnumeric():
#         return False

#     if my_list[0] == my_list[0][::-1] and is_good:
#         is_good = True
#     else:
#         is_good = False

#     if is_prime(int(my_list[1])) and is_good:
#         is_good = True
#     else:
#         is_good = False

#     if int(my_list[2]) % 2 == 0 and is_good:
#         is_good = True
#     else:
#         is_good = False

#     return is_good


# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))


# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))

# # объявление функции
# def is_correct_bracket(text):
#     if text[0] != "(":
#         return False

#     count_left = 0
#     count_right = 0
#     for i in range(len(text)):
#         if text[i] == "(" or text[i] == ")":
#             if text[i] == "(":
#                 count_left += 1
#                 if count_left-count_right < 0:
#                     return False
#             else:
#                 count_right += 1
#                 if count_left-count_right < 0:
#                     return False
#         else:
#             return False

#     return count_left == count_right


# # # считываем данные
# # txt = input()

# # # вызываем функцию
# # print(is_correct_bracket(txt))

# print(is_correct_bracket('((()))'))
# print(is_correct_bracket('(()())'))
# print(is_correct_bracket('(())()'))
# print(is_correct_bracket('()(())'))
# print(is_correct_bracket('()()()'))

# print(is_correct_bracket('()(())()()()(())()(()())((()))'))
# print(is_correct_bracket('()(())()(()())((()))()(())'))
# print(is_correct_bracket('())()()()('))
# print(is_correct_bracket(')))((('))
# print(is_correct_bracket('()(())()((())((()))()(())'))

# print(is_correct_bracket('()(())()(()())((()))()(()'))
# print(is_correct_bracket(')(())()(()())((()))()(())'))
# print(is_correct_bracket('())(()'))
# print(is_correct_bracket(')))'))
# print(is_correct_bracket('(((('))

# print(is_correct_bracket('())((((())))'))

# # объявление функции
# def convert_to_python_case(text):
#     new_str = ''
#     for i in range(len(text)):
#         if i == 0:
#             new_str += text[i].lower()
#         elif text[i].isupper():
#             new_str += "_"+text[i].lower()
#         else:
#             new_str += text[i]
#     return new_str


# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))


# def solve(a, b, c, d, e, f):
#     x = (d * e - b * f)/(a * d - b * c)
#     y = (a * f - c * e)/(a * d - b * c)
#     return x, y


# # xsol, ysol = solve(2, 3, 4, 1, 2, 5)
# print('Решением системы являются числа', 'x =', xsol, 'y =', ysol)

# # объявление функции


# def get_middle_point(x1, y1, x2, y2):
#     x = (x1+x2)/2
#     y = (y1+y2)/2
#     return x, y


# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# print(get_middle_point(0, 0, 10, 0))
# print(get_middle_point(1, 5, 8, 3))
# import math


# def get_circle(radius):
#     l = 2*math.pi * radius
#     s = math.pi * radius**2
#     return l, s


# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)

# def solve(a, b, c):
#     descrim = b**2 - 4*a*c

#     if descrim < 0:
#         return
#     elif descrim == 0:
#         return -b/(2*a), -b/(2*a)
#     elif descrim > 0:
#         x1 = (-b-descrim**0.5)/(2*a)
#         x2 = (-b+descrim**0.5)/(2*a)
#         if x1 <= x2:
#             return x1, x2
#         else:
#             return x2, x1


# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# print(solve(1, -4, -5))
# print(solve(-2, 7, -5))
# print(solve(1, 2, 1))

# # объявление функции
# def draw_triangle():
#     for i in range(1, 9):
#         print(" "*(8-i) + "*"*(i*2 - 1))


# # основная программа
# draw_triangle()  # вызов функции


# # объявление функции
# def get_shipping_cost(quantity):
#     count = 0
#     for i in range(1, quantity+1):
#         if i == 1:
#             count += 1000
#         else:
#             count += 120
#     return count


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_shipping_cost(n))

# объявление функции
# import math


# def compute_binom(n, k):
#     return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))


# # считываем данные
# n = int(input())
# k = int(input())

# # вызываем функцию
# print(compute_binom(n, k))

# zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять',
#                        'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь', 'девяносто девять']


# def number_to_words(num):
#     return zero_to_ninety_nine[num]


#     # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_to_words(n))

# lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#           'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

# lng_en = ['january', 'february', 'march', 'april', 'may', 'june',
#           'july', 'august', 'september', 'october', 'november', 'december']
# # объявление функции


# def get_month(language, number):
#     if language == "ru":
#         return lng_ru[number-1]
#     elif language == "en":
#         return lng_en[number-1]


# # считываем данные
# lan = input()
# num = int(input())

# # вызываем функцию
# print(get_month(lan, num))

# # объявление функции
# def is_magic(date):
#     my_list = date.split(".")
#     date = int(my_list[0])
#     month = int(my_list[1])
#     year = int(my_list[2]) % 100
#     if date * month == year:
#         return True
#     else:
#         return False


# # считываем данные
# date = input()

# # вызываем функцию
# print(is_magic(date))

# объявление функции
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_pangram(text):
    my_text = text.lower()
    count = 0
    for i in range(len(alfabet)):
        if alfabet[i] in my_text:
            count += 1
    return count == len(alfabet)


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
