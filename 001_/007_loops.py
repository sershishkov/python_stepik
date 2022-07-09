# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# for i in range(10):
#     print('Python is awesome!')

# sentence, times = input(), int(input())
# for i in range(times):
#     print(sentence)


# for i in range(6):
#     print("AAA")

# for i in range(6):
#     if i < 5:
#         print("BBBB")
#     else:
#         print("E")

# for i in range(10):
#     if i < 9:
#         print("TTTTT")
#     else:
#         print("G")

# for i in range(6):
#     print(i)

# n = int(input())
# for i in range(n):
#     print("*"*19)

# text = input()
# for i in range(10):
#     print(i, text)

# 3

# n = int(input())
# for i in range(n):
#     print("*"*(n-i))


# m, p, n = int(input()), int(input()), int(input())
# koef = (p/100)+1
# for i in range(n):
#     if i == 0:
#         print(i+1, m)
#     else:
#         m = m*koef
#         print(i+1, m)

# m, n = int(input()), int(input())

# for i in range(m, n+1):
#     print(i)

# m, n = int(input()), int(input())

# if m < n:
#     for i in range(m, n+1):
#         print(i)
# else:
#     for i in range(m, n-1, -1):
#         print(i)

# m, n = int(input()), int(input())

# for i in range(m, n-1, -1):
#     if i % 2 != 0:
#         print(i)

# m, n = int(input()), int(input())

# for i in range(m, n+1):
#     if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# n = int(input())

# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")

# Число простое
# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False

# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# num1 = 4
# num2 = 6
# num1 += num2
# num1 *= num1
# print(num1)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b+1):
#     if (i**3) % 10 == 4 or (i**3) % 10 == 9:
#         counter += 1

# print(counter)

# n = int(input())
# sum = 0
# for i in range(n):
#     sum += int(input())
# print(sum)

# from math import log

# n = int(input())
# sum = 1
# for i in range(2, n+1):
#     sum += 1/i
# print(sum - log(n))

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if (i**2) % 10 == 2 or (i**2) % 10 == 5 or (i**2) % 10 == 8:
#         sum += i
# print(sum)

# n = int(input())
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


# mult = 1
# for _ in range(10):
#     x = int(input())
#     if x != 0:
#         mult *= x
# print(mult)

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         sum += i
# print(sum)

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if i % 2 != 0:
#         sum += i
#     else:
#         sum -= i
# print(sum)

# n = int(input())
# max = -1
# max_sub = -2
# for i in range(n):
#     x = int(input())
#     if x > max:
#         max_sub = max
#         max = x
#     elif x > max_sub:
#         max_sub = x


# print(max)
# print(max_sub)
# is_even = True
# for i in range(10):
#     x = int(input())
#     if x % 2 == 0 and is_even:
#         is_even = True
#     else:
#         is_even = False

# if is_even:
#     print("YES")
# else:
#     print("NO")

# n = int(input())
# prev_number = 1
# current_number = 1
# sum = 2
# if n == 1:
#     print(1)
# elif n == 2:
#     print(1, 1)
# else:
#     print(1, 1, end=' ')
#     for i in range(3, n+1):
#         sum = prev_number + current_number
#         prev_number = current_number
#         current_number = sum
#         print(sum, end=' ')

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)

# count = 1
# while count < 10:
#     print('Python awesome!')
#     count += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# word = input()
# count = 0
# while word != "стоп" and word != "хватит" and word != "достаточно":
#     count += 1
#     word = input()

# print(count)

# number = int(input())
# while number % 7 == 0:
#     print(number)
#     number = int(input())

# number = int(input())
# sum = 0
# while number >= 0:
#     sum += number
#     number = int(input())
# print(sum)

# number = int(input())
# count = 0
# while 0 <= number <= 5:
#     if number == 5:
#         count += 1
#     number = int(input())
# print(count)

# number = int(input())
# count = 0
# while number >= 25:
#     count += 1
#     number -= 25

# while number >= 10:
#     count += 1
#     number -= 10

# while number >= 5:
#     count += 1
#     number -= 5

# while number >= 1:
#     count += 1
#     number -= 1

# print(count)

# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     n = n // 10  # удалить последнюю цифру из числа
#     print(last_digit)


# num = int(input())
# has_seven = False  # сигнальная метка

# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10

# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# n = int(input())
# min = 10
# max = -1
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     if last_digit > max:
#         max = last_digit

#     if last_digit < min:
#         min = last_digit

#     n = n // 10  # удалить последнюю цифру из числа

# print(f"Максимальная цифра равна {max}")
# print(f"Минимальная цифра равна {min}")


# n = int(input())
# last = n % 10
# sum = 0
# count = 0
# mult = 1
# first_digit = 0

# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     sum += last_digit
#     count += 1
#     mult *= last_digit
#     first_digit = last_digit
#     n = n // 10  # удалить последнюю цифру из числа


# print(sum)
# print(count)
# print(mult)
# print(sum/count)
# print(first_digit)
# print(first_digit + last)

# n = int(input())
# second_digit = 0
# while n != 0 and len(str(n)) >= 2:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     second_digit = last_digit
#     n = n // 10  # удалить последнюю цифру из числа
# print(second_digit)

# n = int(input())
# is_the_same = True
# last = n % 10
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     if last_digit == last and is_the_same:
#         is_the_same = True
#     else:
#         is_the_same = False
#     n = n // 10  # удалить последнюю цифру из числа

# if is_the_same:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# is_ordered = True
# prev_digit = n % 10
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     if last_digit >= prev_digit and is_ordered:
#         is_ordered = True
#         prev_digit = last_digit
#     else:
#         is_ordered = False
#     n = n // 10  # удалить последнюю цифру из числа

# if is_ordered:
#     print("YES")
# else:
#     print("NO")

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     if i % 9 == 0:
#         break
#     mult *= i
# print(mult)

# n = int(input())
# delitel = 0
# k = 2
# while True:
#     if n % k == 0:
#         delitel = k
#         break
#     k += 1
# print(delitel)

# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     else:
#         print(i)

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if 0 <= x <= 10**6:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# mx = -10**7
# s = 0
# for i in range(10):
#     x = int(input())
#     if -10**6 <= x < 0:
#         s += x
#     if 0 > x > mx:
#         mx = x

# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# s = 0
# for _ in range(7):
#     n = int(input())
#     if n % 2 == 0 and abs(n) <= 10**6:
#         s += n

# print(s)


# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10

# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# last = 0
# while n > 0:
#     last = n % 10
#     n //= 10
# print(last)


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# for _ in range(n):
#     for _ in range(3):
#         print(n, end=" ")
#     print()

# n = int(input())
# for i in range(1, n+1):
#     for _ in range(5):
#         print(i, end=" ")
#     print()

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, 10):
#         print(f"{i} + {j} = {i+j}")
#     print()

# n = int(input())

# middle = n//2 + 1
# for i in range(1, n+1):
#     if(i <= middle):
#         print("*"*i)
#     else:
#         print("*"*(n-i+1))


# n = int(input())
# for i in range(1, n+1):
#     print(f"{i}"*i)

# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# total = 0
# for n in range(1, 20):
#     for k in range(1, 20):
#         for m in range(1, 20):
#             if n * 28 + k * 30 + m * 31 == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)

# total = 0
# for b in range(1, 100):
#     for k in range(1, 100):
#         for tel in range(1, 100):
#             if b * 10 + k * 5 + tel * 0.5 == 100 and b+k+tel == 100:
#                 print('b =', b, 'k =', k, 'tel =', tel)

# for e in range(1, 151):
#     for a in range(1, 151):
#         for b in range(1, 151):
#             for c in range(1, 151):
#                 for d in range(1, 151):
#                     if e**5 == (a**5 + b**5+c**5+d**5):
#                         print(a, b, c, d, e)

# print(27**5 + 84**5+110**5+133**5, 144**5)
# print(27+84+110+133+144)

# n = int(input())
# count = 0
# for i in range(1, n+1):
#     for _ in range(i):
#         count += 1
#         print(count, end=" ")

#     print()

# n = int(input())
# count = 0
# for i in range(1, n+1):
#     for _ in range(i):
#         count += 1
#         print(count, end=" ")

#     print()

# n = int(input())

# for i in range(1, n+1):
#     print((int("1"*i))**2)

# n = int(input())

# for i in range(n):
#     diff = 1
#     for j in range(1, i + i + 2):
#         if j <= i+1:
#             print(j, end='')
#         else:
#             print(i+1-diff, end='')
#             diff += 1

#     print()

# a, b = int(input()), int(input())
# sum = 0
# digit = -1
# for i in range(a, b + 1):
#     temp_sum = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             temp_sum += j

#     if temp_sum >= sum:
#         sum = temp_sum
#         digit = i

# print(digit, sum)

# n = int(input())
# for i in range(1, n+1):
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     print(i, "+"*count, sep='')

# n = int(input())
# if n % 9 == 0:
#     print(9)
# else:
#     print(n % 9)

# from math import *
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += factorial(i)

# print(sum)

# a, b = int(input()), int(input())

# for i in range(a, b+1):
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     if count <= 2:
#         if i == 1:
#             continue
#         else:
#             print(i)

# year = int(input())

# if year % 100 == 0:
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# color1 = ""
# color2 = ""

# if (x1 % 2 == 0 and y1 % 2 == 0) or (x1 % 2 != 0 and y1 % 2 != 0):
#     color1 = "black"
# else:
#     color1 = "white"

# if (x2 % 2 == 0 and y2 % 2 == 0) or (x2 % 2 != 0 and y2 % 2 != 0):
#     color2 = "black"
# else:
#     color2 = "white"

# if color1 == color2:
#     print("YES")
# else:
#     print("NO")

# age, gender = int(input()), input()

# if 10 <= age <= 15 and gender == "f":
#     print("YES")
# else:
#     print("NO")

# digit = input()

# if digit == '1':
#     print("I")
# elif digit == '2':
#     print("II")
# elif digit == '3':
#     print("III")
# elif digit == '4':
#     print("IV")
# elif digit == '5':
#     print("V")
# elif digit == '6':
#     print("VI")
# elif digit == '7':
#     print("VII")
# elif digit == '8':
#     print("VIII")
# elif digit == '9':
#     print("IX")
# elif digit == '10':
#     print("X")
# else:
#     print("ошибка")

# digit = int(input())
# if digit % 2 != 0:
#     print("YES")
# elif digit % 2 == 0 and 2 <= digit <= 5:
#     print("NO")
# elif digit % 2 == 0 and 6 <= digit <= 20:
#     print("YES")
# elif digit % 2 == 0 and digit > 20:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# delta_x = abs(x2 - x1)
# delta_y = abs(y2 - y1)

# if delta_x - delta_y == 0:
#     print("YES")
# else:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())


# if (abs(y2-y1) == 2 and abs(x2-x1) == 1) or (abs(y2-y1) == 1 and abs(x2-x1) == 2):
#     print("YES")
# else:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# delta_x = abs(x2 - x1)
# delta_y = abs(y2 - y1)
# if (delta_x == 0) or (delta_y == 0) or (delta_x - delta_y == 0):
#     print("YES")
# else:
#     print("NO")

# for i in range(10, 25):
#     print('Python awesome!')


# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 7 != 0:
#         counter += 1
# print(counter)

# i = 4
# while i <= 10:
#     print('Python!')
#     i += 1

# n = int(input())
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(res)

# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)


# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)


# n = 8
# count = 0
# maximum = -10**12-1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# n = 4
# count = 0
# maximum = -10**8-1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())

# for i in range(n):
#     if i == 0 or i == n-1:
#         print("*"*19)
#     else:
#         print("*", " "*17, "*", sep='')

# n = input()
# print(int(n[2]))

# n = int(input())
# last_digit = n % 10
# count_3 = 0
# count_last_digit = 0
# count_even = 0
# sum_more_than_5 = 0
# mult_more_than_7 = 1
# count_0_or_5 = 0

# while n > 0:
#     last = n % 10
#     if last == 3:
#         count_3 += 1

#     if last == last_digit:
#         count_last_digit += 1

#     if last % 2 == 0:
#         count_even += 1

#     if last > 5:
#         sum_more_than_5 += last

#     if last > 7:
#         mult_more_than_7 *= last

#     if last == 0 or last == 5:
#         count_0_or_5 += 1

#     n //= 10

# print(count_3)
# print(count_last_digit)
# print(count_even)
# print(sum_more_than_5)
# print(mult_more_than_7)
# print(count_0_or_5)


for i in range(1729, 35000):
    for a in range(1, 33):
        for b in range(1, 33):
            for c in range(1, 33):
                for d in range(1, 33):
                    if (a**3 + b**3 == c**3 + d**3 == i) and (a != b and a != c and a != d and b != c and b != d and c != d) and (a < b and c < d):
                        print(i, a, b, c, d)
