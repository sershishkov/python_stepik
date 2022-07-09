# n = int(input())
# my_list = list(range(1, n+1))
# print(my_list)

# n = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# new_abc = abc[:n]
# print(new_abc)


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#           31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[16])

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#           31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[len(primes)-1])

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#           31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[:6])


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

# print(min(numbers)+max(numbers))


# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens)/len(evens)

# print(average)


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = "Зеленый"
# rainbow[6] = "Фиолетовый"
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic',
#              'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

# print(languages[::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]

# print(numbers1*2 + numbers2*9 + numbers3)


# numbers = []  # создаем пустой список

# numbers.append(1)
# numbers.append(2)
# numbers.append(3)

# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[5]    # удаляем элемент имеющий индекс 5

# print(numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[2:7]    # удаляем элементы с 2 по 6 включительно

# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[::2]

# print(numbers)


# numbers = [4, 2]
# numbers.extend([1, 2, 3])
# numbers.extend([7, 17, 777])
# print(numbers)


# colors = ['red', 'orange', 'yellow', 'green',
#           'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
# print(colors)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10,
#            10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[len(numbers)-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# print(numbers[1:len(numbers)-1])


# n = int(input())
# my_list = []
# for _ in range(n):
#     str_text = input()
#     my_list.append(str_text)

# print(my_list)

# my_list = []
# for i in range(97, 123):
#     my_list.append(chr(i)*(i-96))

# print(my_list)

# n = int(input())
# my_list = []
# for _ in range(n):
#     number = int(input())
#     my_list.append(number**3)

# print(my_list)

# n = int(input())
# my_list = []
# for i in range(1, n+1):
#     if n % i == 0:
#         my_list.append(i)

# print(my_list)

# n = int(input())
# my_list = []
# list_sum = []
# for i in range(n):
#     n = int(input())
#     my_list.append(n)

# for i in range(1, len(my_list)):
#     list_sum.append(my_list[i-1]+my_list[i])

# print(list_sum)

# n = int(input())
# my_list = []
# for i in range(n):
#     n = int(input())
#     my_list.append(n)

# print(my_list[::2])

# n = int(input())
# my_list = []
# for i in range(n):
#     text = input()
#     my_list.append(text)

# k = int(input())
# new_str = ''
# for i in range(len(my_list)):
#     if len(my_list[i]) >= k:
#         new_str += my_list[i][k-1]

# print(new_str)


# n = int(input())
# my_list = []
# for i in range(n):
#     text = input()
#     my_list.extend(text)

# print(my_list)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     print(num, end=' ')

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(*numbers)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(*numbers, sep='\n')

# s = 'Python'

# print(*s)
# print()
# print(*s, sep='\n')

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sum = 0
# for num in numbers:
#     sum += num**2
# print(sum)

# n = int(input())
# inputs_list = []
# results_list = []
# for i in range(n):
#     x = int(input())
#     inputs_list.append(x)
#     results_list.append(x**2 + 2*x + 1)

# for input in inputs_list:
#     print(input, sep='\n')
# print()
# for result in results_list:
#     print(result, sep='\n')


# n = int(input())
# my_list = []

# for i in range(n):
#     x = int(input())
#     my_list.append(x)

# my_list.remove(max(my_list))
# my_list.remove(min(my_list))


# for item in my_list:
#     print(item, sep='\n')


# n = int(input())
# my_list = []
# for i in range(n):
#     x = input()
#     if x not in my_list:
#         my_list.append(x)
# for item in my_list:
#     print(item, sep='\n')


# n = int(input())
# my_list = []
# filtered_list = []
# for i in range(n):
#     sentence = input()
#     my_list.append(sentence)
# search_word = input()

# for i in range(len(my_list)):
#     if search_word.lower() in my_list[i].lower():
#         filtered_list.append(my_list[i])
# for item in filtered_list:
#     print(item, sep='\n')

# n = int(input())
# my_list = []
# search_list = []
# filtered_list = []
# for i in range(n):
#     sentence = input()
#     my_list.append(sentence)
# k = int(input())
# for j in range(k):
#     search_word = input()
#     search_list.append(search_word)

# for i in range(len(my_list)):
#     count = 0
#     for j in range(len(search_list)):
#         if search_list[j].lower() in my_list[i].lower():
#             count += 1
#     if count == len(search_list):
#         filtered_list.append(my_list[i])


# for item in filtered_list:
#     print(item, sep='\n')


# n = int(input())
# my_list = []
# for _ in range(n):
#     x = int(input())
#     my_list.append(x)


# for item in my_list:
#     if item < 0:
#         print(item, sep='\n')
# for item in my_list:
#     if item == 0:
#         print(item, sep='\n')
# for item in my_list:
#     if item > 0:
#         print(item, sep='\n')

# ip = '192.168.1.24'
# numbers = ip.split('.')    # указываем явно разделитель
# print(numbers)


# words = ['Мы', 'учим', 'язык', 'Python']
# print('*'.join(words))
# print('-'.join(words))
# print('?'.join(words))
# print('!'.join(words))
# print('*****'.join(words))
# print('abc'.join(words))
# print('123'.join(words))


# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# sentence = input()
# my_list = sentence.split()

# for item in my_list:
#     print(item, sep='\n')

# sentence = input()
# my_list = sentence.split()

# for item in my_list:
#     print(item[0], end=".")

# sentence = input()
# my_list = sentence.split('\\')

# for item in my_list:
#     print(item, sep='\n')

# sentence = input()
# my_list = sentence.split(' ')

# for item in my_list:
#     print("+"*int(item), sep='\n')

# ip = input()
# my_list = ip.split('.')

# count = 0
# for item in my_list:
#     if 0 <= int(item) <= 255:
#         count += 1
# if count == 4:
#     print('ДА')
# else:
#     print("НЕТ")

# sentence = input()
# devider = input()
# my_list = list(sentence)
# new_str = devider.join(my_list)
# print(new_str)


# sentence = input()
# my_list = sentence.split(" ")
# count = 0
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             count += 1

# print(count)

# sentence = input()
# my_list = sentence.split(" ")
# count = 0
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             count += 1

# print(count)

# names = ['Gvido', 'Roman', 'Timur']
# position = names.index('Timur')
# print(position)

# names = ['Gvido', 'Roman', 'Timur']
# if 'Anders' in names:
#     position = names.index('Anders')
#     print(position)
# else:
#     print('Такого значения нет в списке')


# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# print(food)
# food.remove('Рис')
# print(food)

# names = ['Gvido', 'Roman', 'Timur']
# item = names.pop(1)
# print(item)
# print(names)

# names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
# cnt1 = names.count('Timur')
# cnt2 = names.count('Gvido')
# cnt3 = names.count('Josef')

# print(cnt1)
# print(cnt2)
# print(cnt3)

# names = ['Gvido', 'Roman', 'Timur']
# names.reverse()
# print(names)

# names = ['Gvido', 'Roman', 'Timur']
# names.clear()
# print(names)

# names = ['Gvido', 'Roman', 'Timur']
# names_copy = names.copy()              # создаем поверхностную копию списка names

# print(names)
# print(names_copy)

# colors = ['Orange']
# colors.append('Red')
# colors.append('Blue')
# colors.append('Green')
# colors.insert(0, 'Violet')
# colors.insert(2, 'Purple')

# print(colors)

# colors = ['Red', 'Blue', 'Green', 'Black', 'White']
# del colors[-1]
# colors.remove('Green')

# print(colors)


# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)

# # for item in numbers:
# #     print(item, sep='\n')

# print(*numbers)

# my_list = input().split(' ')
# list_max = max(my_list, key=int)
# list_min = min(my_list, key=int)
# index_max = my_list.index(list_max)
# index_min = my_list.index(list_min)
# my_list[index_max] = list_min
# my_list[index_min] = list_max
# print(*my_list)

# my_list = input().lower().split()
# total_count = my_list.count('a') + my_list.count('an') + my_list.count('the')
# print(f"Общее количество артиклей: {total_count}")


# text = input()
# num = int(text[1:])

# for i in range(num):
#     sentence = input()
#     if "#" in sentence:
#         print(sentence[:sentence.index("#")].rstrip())
#     else:
#         print(sentence.rstrip())


# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# a.sort()
# print('Отсортированный список:', a)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# a.sort(reverse=True)   # сортируем по убыванию
# print('Отсортированный список:', a)

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers)

# my_list = input().split(' ')
# int_lst = [int(x) for x in my_list]
# int_lst.sort()
# print(*int_lst)
# int_lst.sort(reverse=True)
# print(*int_lst)

# zeros = [0 for i in range(10)]
# print(*zeros)

# squares = [i ** 2 for i in range(10)]
# print(*squares)

# cubes = [i ** 3 for i in range(10, 21)]
# print(*cubes)

# chars = [c for c in 'abcdefg']
# print(chars)


# n = int(input())
# lines = [input() for _ in range(n)]

# lines = [input() for _ in range(int(input()))]

# numbers = [int(input()) for _ in range(int(input()))]

# evens = [i for i in range(21) if i % 2 == 0]
# print(evens)

# numbers = [i * j for i in range(1, 5) for j in range(2)]
# print(numbers)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#             'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [key[1:] for key in keywords]

# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#             'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# lengths = [len(key) for key in keywords]

# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#             'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [key for key in keywords if len(key) >= 5]

# print(new_keywords)

# palindromes = [number for number in range(
#     100, 1001) if number % 10 == number//100]

# print(palindromes)


# numbers = [i**2 for i in range(1, int(input())+1)]

# for item in numbers:
#     print(item, sep="\n")

# text_digit = input().split(" ")
# list_digits = [int(x)**3 for x in text_digit]
# for item in list_digits:
#     print(item, end=" ")

# my_list = input().split()
# for item in my_list:
#     print(item, sep="\n")

# print(*[i for i in input().split()], sep="\n")

# from curses.ascii import isdigit


# print(*[i for i in list(input()) if i.isnumeric()], sep="")

# print(*[int(i)**2 for i in input().split(" ")
#       if int(i) % 2 == 0 and int(i)**2 % 10 != 4])

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# сортировка пузырьком
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами

# print('Отсортированный список:', a)

# сортировка выбором
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56,
#      71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)

# for i in range(n-1):
#     for k in range(i+1, n):
#         if a[k] < a[i]:
#             a[k], a[i] = a[i], a[k]

# print(a)

# сортировка простыми вставками:
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)

# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem


# print('Отсортированный список:', a)


# numbers = [1, 2, 3, 4, 5]
# numbers[2] = 99
# print(numbers)

# numbers = list(range(3))
# print(numbers)

# numbers = [10] * 5
# print(numbers)

# numbers = list(range(1, 10, 2))
# for i in numbers:
#     print(i, end='*')

# numbers = [1, 2, 3, 4, 5]
# print(numbers[-2])

# numbers1 = [1, 2, 3]
# numbers2 = [10, 20, 30]
# numbers3 = numbers1 + numbers2
# print(numbers3)

# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[1:3]
# print(my_list)

# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[1:]
# print(my_list)

# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:-1]
# print(my_list)

# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:]
# print(my_list)

# names = ['Джим', 'Джилл', 'Джон', 'Джасмин']
# if 'Джасмин' not in names:
#     print('Не могу найти Джасмин.')
# else:
#     print('Ceмья Джасмин: ', end='')
#     print(names)

# my_list = [i for i in range(2, int(input())+1, 2)]
# print(my_list)


# list_n = input().split(" ")
# list_m = input().split(" ")

# list_sum = [int(list_n[i]) + int(list_m[i]) for i in range(len(list_n))]
# print(*list_sum)

# list_n = input().split(" ")
# list_int = [int(list_n[i]) for i in range(len(list_n))]
# sum_list = sum(list_int)

# print(f"{'+'.join(list_n)}={sum_list}")

# text = input()
# digits = text.split("-")
# is_correct = True

# if (len(digits) == 4 or len(digits) == 3):
#     is_correct = True
# else:
#     is_correct = False


# for item in digits:
#     if item.isnumeric() and is_correct:
#         is_correct = True
#     else:
#         is_correct = False


# if len(digits) == 4:
#     if digits[0] == "7" and len(digits[1]) == 3 and len(digits[2]) == 3 and len(digits[3]) == 4 and is_correct:
#         is_correct = True
#     else:
#         is_correct = False


# if len(digits) == 3:
#     if len(digits[0]) == 3 and len(digits[1]) == 3 and len(digits[2]) == 4 and is_correct:
#         is_correct = True
#     else:
#         is_correct = False

# if is_correct:
#     print("YES")
# else:
#     print("NO")


# list_len = [len(item) for item in input().split()]
# print(max(list_len))

# new_list = [item[1:]+item[0]+'ки' for item in input().split()]
# print(*new_list)
