# print('Здравствуй, мир!')
# print(4, 8, 15, 16, 23, 42)

# print('a', 'b', 'c', sep='*', end='finish')
# print('d', 'e', 'f', sep='**', end='^__^')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='#')
# print('m', 'n', 'o', sep='/', end='!')

# print('Mercury', 'Venus', sep='*', end='!')
# print('Mars', 'Jupiter', sep='**', end='?')

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
# print('I', 'like', 'Python', sep='***')

# input_sep = input()
# str1 = input()
# str2 = input()
# str3 = input()
# print(str1, str2, str3, sep=input_sep)

# name = input()
# print("Привет,", name, end="!")  # ;lkj;lkj;lkj

# # print('Java')
# # print('Ruby')
# # print('Scala')
# print('Python', end='+')  # print('C++')
# # print('GO')
# print('C#', end='=')  # print('C')
# print('awesome')
# # finish

# s = 0
# k = 30
# d = k - 5
# k = 2 * d
# s = k - 100

# print(s)

# x = 3
# y = 4
# z = x + y
# z = z + 1
# x = y
# y = 5
# x = z + y + 7
# print(x)

# number = int(input())
# print(number)
# print(number+1)
# print(number+2)

# number1 = int(input())
# number2 = int(input())
# number3 = int(input())

# print(number1+number2+number3)

# number1 = int(input())
# print("Объем =", number1*number1*number1)
# print("Площадь полной поверхности =", 6*number1*number1)

# a = int(input())
# b = int(input())
# print(3*((a+b)**3) + 275*b*b - 127*a - 41)

# number = int(input())
# print("Следующее за числом", number, "число:", number+1)
# print("Для числа", number, "предыдущее число:", number-1)

# monitor = int(input())
# block = int(input())
# klava = int(input())
# mouse = int(input())
# print((monitor+block+klava+mouse)*3)

# left = int(input())
# right = int(input())
# print(left, "+", right, '=', left+right)
# print(left, "-", right, '=', left-right)
# print(left, "*", right, '=', left*right)

# a1 = int(input())
# d = int(input())
# n = int(input())
# print(a1+d*(n-1))

# x = int(input())
# print(x, 2*x, 3*x, 4*x, 5*x, sep="---")

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

# a = 82 // 3 ** 2 % 7
# print(a)

# b1 = int(input())
# q = int(input())
# n = int(input())

# print(b1*q**(n-1))

# sm = int(input())
# print(sm//100)

# people = int(input())
# mandarin = int(input())
# print(mandarin // people)
# print(mandarin % people)

# people = int(input())
# survived = people
# if people % 2 != 0:
#     survived = people//2 + 1
# else:
#     survived = int(people/2)
# print(survived)

# number = int(input())
# kupe = 0
# if number <= 4:
#     kupe = 1
# elif number % 4 == 0:
#     kupe = number//4
# else:
#     kupe = number//4 + 1

# print(kupe)

# total_minutes = int(input())
# hours = total_minutes//60
# minutes = total_minutes % 60
# print(total_minutes, "мин - это", hours, "час", minutes, "минут.")

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Сумма цифр =', last_digit + first_digit)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')

# number = int(input())
# digit_0 = number % 10
# digit_00 = (number // 10) % 10
# digit_000 = number // 100
# print('Сумма цифр =', digit_000+digit_00+digit_0)
# print('Произведение цифр =', digit_000*digit_00*digit_0)

# number = int(input())
# c = number % 10
# b = (number // 10) % 10
# a = number // 100
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')


# number = int(input())
# digit_ed = number % 10
# digit_dec = (number // 10) % 10
# digit_sot = (number // 100) % 10
# digit_tys = number // 1000
# print("Цифра в позиции тысяч равна", digit_tys)
# print("Цифра в позиции сотен равна", digit_sot)
# print("Цифра в позиции десятков равна", digit_dec)
# print("Цифра в позиции единиц равна", digit_ed)


# num1 = int(input())
# num2 = int(input())

# if num1 < num2:
#     print(num1, 'меньше чем', num2)
# if num1 > num2:
#     print(num1, 'больше чем', num2)
# if num1 == num2:
#     print(num1, 'равно', num2)
# if num1 != num2:
#     print(num1, 'не равно', num2)

# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# password, confirm_password = input(), input()
# if password == confirm_password:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# number = int(input())
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# number = int(input())
# digit_ed = number % 10
# digit_dec = (number // 10) % 10
# digit_sot = (number // 100) % 10
# digit_tys = number // 1000
# if (digit_tys+digit_ed) == (digit_sot-digit_dec):
#     print("ДА")
# else:
#     print("НЕТ")

# age = int(input())
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# num1, num2, num3 = int(input()), int(input()), int(input())
# if (num2 - num1) == (num3 - num2):
#     print("YES")
# else:
#     print("NO")

# num1, num2 = int(input()), int(input())
# if num1 < num2:
#     print(num1)
# else:
#     print(num2)

# num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())

# minLeft = 0
# minRight = 0
# minTotal = 0
# if num1 < num2:
#     minLeft = num1
# else:
#     minLeft = num2

# if num3 < num4:
#     minRight = num3
# else:
#     minRight = num4

# if minLeft < minRight:
#     minTotal = minLeft
# else:
#     minTotal = minRight

# print(minTotal)

# age = int(input())
# if age <= 13:
#     print("детство")
# elif 13 < age <= 24:
#     print("молодость")
# elif 24 < age <= 59:
#     print("зрелость")
# else:
#     print("старость")

# num1, num2, num3 = int(input()), int(input()), int(input())
# sum = 0
# if num1 > 0:
#     sum = sum+num1

# if num2 > 0:
#     sum = sum + num2

# if num3 > 0:
#     sum = sum + num3

# print(sum)

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
# num = int(input())
# d3 = num % 10
# d2 = num % 100 // 10
# d1 = num // 100
# if d3 != d2 and d3 != d1 and d2 != d1:
#     print('Цифры различны')
# else:
#     print('Цифры не различны')


# Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанному промежутку:(-1:17)
# x = int(input())
# if x > -1 and x < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.
# x = int(input())
# if x <= -3 or x >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.
# x = int(input())
# if (x > -30 and x <= -2) or (x > 7 and x <= 25):
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
# x = int(input())

# if len(str(x)) == 4 and ((x % 7 == 0) or (x % 17 == 0)):
#     print('YES')
# else:
#     print('NO')


# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
# x, y, z = int(input()), int(input()), int(input())

# if (x < (y + z)) and (y < (x + z)) and (z < (x + y)):
#     print('YES')
# else:
#     print('NO')

# Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# year = int(input())

# if year % 4 == 0 and ((not year % 100 == 0) or (year % 400 == 0)):
#     print('YES')
# else:
#     print('NO')

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
# На вход программе подаётся четыре числа от 1 до 8.

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')

# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
# На вход программе подаётся четыре числа от 1 до 8.

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (abs(x2-x1) == 1 and (abs(y2-y1) == 1 or y2-y1 == 0)) or (abs(x2-x1) == 0 and abs(y2-y1) == 1):
#     print('YES')
# else:
#     print('NO')


# zoom, flesh = int(input()), int(input())

# if flesh > zoom:
#     print("YES")
# elif flesh < zoom:
#     print("NO")
# else:
#     print("Don't know")

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# На вход программе подаются три числа – длины сторон существующего треугольника.
# Программа должна вывести на экран текст – вид треугольника(«Равносторонний», «Равнобедренный» или «Разносторонний»).

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print("Равносторонний")
# elif a == b != c or a != b == c or b != a == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
# Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.
# a, b, c = int(input()), int(input()), int(input())
# if ((a < b) and (b < c)) or ((c < b) and (b < a)):
#     print(b)
# elif ((b < a) and (a < c)) or ((c < a) and (a < b)):
#     print(a)
# else:
#     print(c)

# Дан порядковый номер месяца(1, \, 2, \ldots, 12)(1, 2, …, 12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
# month_number = int(input())
# if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
#     print(31)
# elif month_number == 2:
#     print(28)
# else:
#     print(30)

# Известен вес боксера-любителя(целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг
# Полусредний вес – до 69 кг.

# Напишите программу, определяющую, в какой категории будет выступать данный боксер.
# weight = int(input())
# if weight < 60:
#     print("Легкий вес")
# elif 60 <= weight < 64:
#     print("Первый полусредний вес")
# elif 64 <= weight < 69:
#     print("Полусредний вес")


# Calculator
# left = int(input())
# right = int(input())
# operator = input()

# if operator == "+" or operator == "-" or operator == "*" or operator == "/":
#     if operator == "+":
#         print(left + right)
#     elif operator == "-":
#         print(left - right)
#     elif operator == "*":
#         print(left * right)
#     elif operator == "/":
#         if right == 0:
#             print("На ноль делить нельзя!")
#         else:
#             print(left / right)
# else:
#     print("Неверная операция")


# Смешиваем политру
# base_color_1 = input()
# base_color_2 = input()


# if (base_color_1 == "красный" or base_color_1 == "синий" or base_color_1 == "желтый") and (base_color_2 == "красный" or base_color_2 == "синий" or base_color_2 == "желтый"):
#     if (base_color_1 == "красный" and base_color_2 == "синий") or (base_color_2 == "красный" and base_color_1 == "синий"):
#         print("фиолетовый")
#     elif (base_color_1 == "красный" and base_color_2 == "желтый") or (base_color_2 == "красный" and base_color_1 == "желтый"):
#         print("оранжевый")
#     elif (base_color_1 == "синий" and base_color_2 == "желтый") or (base_color_2 == "синий" and base_color_1 == "желтый"):
#         print("зеленый")

#     elif (base_color_1 == "синий" and base_color_2 == "синий"):
#         print("синий")
#     elif (base_color_1 == "желтый" and base_color_2 == "желтый"):
#         print("желтый")
#     elif (base_color_1 == "красный" and base_color_2 == "красный"):
#         print("красный")
# else:
#     print("ошибка цвета")


# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
# карман 0 зеленый
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.


# guess_number = int(input())

# if guess_number > 36 or guess_number < 0:
#     print("ошибка ввода")
# elif guess_number == 0:
#     print("зеленый")
# elif guess_number >= 1 and guess_number <= 10:
#     if guess_number % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif guess_number >= 11 and guess_number <= 18:
#     if guess_number % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif guess_number >= 19 and guess_number <= 28:
#     if guess_number % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif guess_number >= 29 and guess_number <= 36:
#     if guess_number % 2 == 0:
#         print("красный")
#     else:
#         print("черный")


# Пересечение отрезков
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())


# def intersection(a1, b1, a2, b2, right_amnswer):
#     print(right_amnswer, end="")
#     if a2 > b1 or a1 > b2:
#         print("пустое множество")

#     # с одинаковыми координатами
#     elif a1 == a2 and b1 == b2:
#         print(a2, b2, "с одинаковыми координатами")

#     # внутри другого
#     elif a1 < a2 and b1 > b2:
#         print(a2, b2, "внутри другого 1")
#     elif a1 > a2 and b1 < b2:
#         print(a1, b1, "внутри другого 2")

#     # стык
#     elif b1 == a2:
#         print(b1, "стык 1")
#     elif b2 == a1:
#         print(b2, "стык 2")

#     # пересечение
#     elif a1 < a2 and a2 < b1 and b1 < b2:
#         print(a2, b1, "пересечение 1")
#     elif a2 < a1 and a1 < b2 and b2 < b1:
#         print(a1, b2, "пересечение 2")

#     # внутри с общей стороной (первый внутри второго)
#     elif (a1 == a2 and b1 < b2) or (a1 < a2 and b1 == b2):
#         print(a1, b1, "внутри с общей стороной (1вый внутри второго)")

#     # внутри с общей стороной (второй внутри первого)
#     elif (a1 < a2 and b1 == b2) or (a1 == a2 and b2 < b1):
#         print(a2, b2, "внутри с общей стороной (второй внутри первого)")


# intersection(1, 5, 6, 10, "#пустое множество:  ")
# intersection(6, 10, 1, 5, "#пустое множество:  ")
# intersection(1, 5, 1, 5, "#1 5:  ")
# intersection(1, 10, 3, 5, "#3 5:  ")
# intersection(3, 5, 1, 10, "#3 5:  ")

# intersection(5, 10, 1, 5, "#5:  ")
# intersection(1, 5, 5, 10, "#5:  ")
# intersection(1, 5, 3, 7, "#3 5:  ")
# intersection(3, 7, 1, 5, "#3 5:  ")
# intersection(1, 5, 1, 10, "#1 5:  ")
# intersection(5, 10, 1, 10, "###5 10:  ")
# # intersection(1, 10, 5, 10, "#rrr5 10:  ")
# intersection(1, 10, 1, 5, "#1 5:  ")
##############################################################################

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a1 < b1 < a2 < b2) or (a2 < b2 < a1 < b1):
#     print("пустое множество")

# # с одинаковыми координатами
# elif a1 == a2 and b1 == b2:
#     print(a2, b2)

# # внутри другого
# elif a1 < a2 < b2 < b1:
#     print(a2, b2)
# elif a2 < a1 < b1 < b2:
#     print(a1, b1)

# # пересечение
# elif a1 < a2 < b1 < b2:
#     print(a2, b1)
# elif a2 < a1 < b2 < b1:
#     print(a1, b2)

# # стык
# elif a1 < b1 == a2 < b2:
#     print(b1)
# elif a2 < b2 == a1 < b1:
#     print(b2)

# # внутри с общей стороной (1вый внутри второго)
# elif (a1 == a2 < b1 < b2) or (a2 < a1 < b2 == b1):
#     print(a1, b1)

# # внутри с общей стороной (второй внутри первого)
# elif (a1 < a2 < b1 == b2) or (a1 == a2 < b2 < b1):
#     print(a2, b2)
# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)

# print("*", "*", "*", "*", "*", "*", "*", "*",
#       "*", "*", "*", "*", "*", "*", "*", "*", "*", sep='')
# print("*", " ", " ", " ", " ", " ", " ", " ",
#       " ", " ", " ", " ", " ", " ", " ", " ", "*", sep='')
# print("*", " ", " ", " ", " ", " ", " ", " ",
#       " ", " ", " ", " ", " ", " ", " ", " ", "*", sep='')
# print("*", "*", "*", "*", "*", "*", "*", "*",
#       "*", "*", "*", "*", "*", "*", "*", "*", "*", sep='')

# a, b = int(input()), int(input())
# print("Квадрат суммы", a, "и", b, "равен", (a+b)**2)
# print("Сумма квадратов", a, "и", b, "равна", a**2 + b**2)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(a**b + c**d)

# n = int(input())
# print(n + (n*10 + n)+(n*100 + n*10 + n))
# a, b = float(input()), float(input())
# print((a*b)/2)

# s, v1, v2 = float(input()), float(input()), float(input())
# print(s/(v1+v2))

# number = float(input())
# if number == 0:
#     print("Обратного числа не существует")
# else:
#     print(1/number)

# f = float(input())
# print((f-32)*5/9)

# dog_years = float(input())
# if dog_years <= 2:
#     print(dog_years*10.5)
# else:
#     print(2*10.5 + (dog_years - 2)*4)

# number = float(input())
# rest = int(number*10) % 10
# print(rest)

# number = float(input())
# my_int = int(number)
# print(number - my_int)

# num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
# print(num)

# num1, num2, num3, num4, num5 = int(input()), int(
#     input()), int(input()), int(input()), int(input())
# print("Наименьшее число =", min(num1, num2, num3, num4, num5))
# print("Наибольшее число =", max(num1, num2, num3, num4, num5))

# num1, num2, num3 = int(input()), int(input()), int(input())
# min = min(num1, num2, num3)
# max = max(num1, num2, num3)
# middle = num1 + num2 + num3 - max - min
# print(max)
# print(middle)
# print(min)

# number = int(input())
# d3 = number % 10
# d2 = (number % 100) // 10
# d1 = number//100

# min = min(d1, d2, d3)
# max = max(d1, d2, d3)
# middle = d1 + d2 + d3 - max - min


# if middle == (max-min):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# num1, num2, num3, num4, num5 = float(input()), float(
#     input()), float(input()), float(input()), float(input())

# print(abs(num1)+abs(num2)+abs(num3)+abs(num4)+abs(num5))

# p1, p2, q1, q2 = int(input()), int(
#     input()), int(input()), int(input())

# print(abs(p1-q1)+abs(p2-q2))

# print('-' * 75)
# mystr = 'да'
# mystr = mystr + 'нет'
# mystr = mystr + 'да'
# print(mystr)

# str1 = '1'
# str2 = str1 + '2' + str1
# str3 = str2 + '3' + str2
# str4 = str3 + '4' + str3
# print(str4)

# mystr = '123' * 3 + '456' * 2 + '789' * 1
# print(mystr)
# str1 = '"Python is a great language!", said Fred. '
# str2 = '"I don\'t ever remember having this much fun before."'
# print(str1+str2)

# firstname = input()
# lastname = input()
# print("Hello "+firstname+" "+lastname+"! You just delved into Python")

# team_name = input()
# print(f"Футбольная команда {team_name} имеет длину {len(team_name)} символов")

# city1, city2, city3 = input(), input(), input()
# min = min(len(city1), len(city2), len(city3))
# max = max(len(city1), len(city2), len(city3))

# if len(city1) == min:
#     print(city1)
# elif len(city2) == min:
#     print(city2)
# else:
#     print(city3)

# if len(city1) == max:
#     print(city1)
# elif len(city2) == max:
#     print(city2)
# else:
#     print(city3)


# word1, word2, word3 = input(), input(), input()
# min = min(len(word1), len(word2), len(word3))
# max = max(len(word1), len(word2), len(word3))
# middle = len(word1) + len(word2) + len(word3) - min - max

# if max - middle == middle - min:
#     print("YES")
# else:
#     print("NO")

# sentence = input()
# find_color = "синий"
# if find_color in sentence:
#     print("YES")
# else:
#     print("NO")


# sentence = input()
# saturday = "суббота"
# sunday = "воскресенье"
# if saturday in sentence or sunday in sentence:
#     print("YES")
# else:
#     print("NO")

# sentence = input()
# mySep1 = "@"
# mySep2 = "."
# if mySep1 in sentence and mySep2 in sentence:
#     print("YES")
# else:
#     print("NO")


# from math import *

# x1, y1, x2, y2 = float(input()), float(
#     input()), float(input()), float(input())

# result = sqrt((x1-x2)**2 + (y1-y2)**2)
# print(result)

# from math import *

# r = float(input())

# s = pi*(r**2)
# l = pi*r*2
# print(s)
# print(l)

# from math import *
# a, b = float(input()), float(input())

# print((a+b)/2)
# print(sqrt(a*b))
# print(2*a*b/(a+b))
# print(sqrt((a**2 + b**2)/2))

# from math import *
# x = float(input())
# r = x*pi/180
# print(sin(r)+cos(r)+(tan(r))**2)

# from math import *
# x = float(input())
# print(ceil(x)+floor(x))

# from math import *
# a, b, c = float(input()), float(input()), float(input())
# descrim = b**2 - 4*a*c

# if descrim < 0:
#     print("Нет корней")
# elif descrim == 0:
#     print(-b/(2*a))
# elif descrim > 0:
#     x1 = (-b-descrim**0.5)/(2*a)
#     x2 = (-b+descrim**0.5)/(2*a)
#     if x1 <= x2:
#         print(x1)
#         print(x2)
#     else:
#         print(x2)
#         print(x1)

# from math import *
# n, a = int(input()), float(input())

# print((n * a**2)/(4*tan(pi/n)))

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1
