# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

# print(emoji.emojize('Python is :bowtie:'))
# print(emoji.emojize("Python is fun :red_heart:"))

# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')

# s = 'abcdefg'
# print(s[0] + s[2] + s[4] + s[6])

# s = 'abcdefg'
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# print(s[7])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# print(s[-10])

# some_text = input()

# for i in range(len(some_text)):
#     if i % 2 == 0:
#         print(some_text[i])

# some_text = input()

# for i in range(len(some_text)-1, -1, -1):
#     print(some_text[i])

# name, last_name, second_name = input(), input(), input()

# print(last_name[0], name[0], second_name[0], sep='')

# some_number_text = input()
# sum = 0
# for i in range(len(some_number_text)):
#     sum += int(some_number_text[i])
# print(sum)

# some_text = input()
# if "0" in some_text or "1" in some_text or "2" in some_text or "3" in some_text or "4" in some_text or "5" in some_text or "6" in some_text or "7" in some_text or "8" in some_text or "9" in some_text:
#     print("Цифра")
# else:
#     print("Цифр нет")

# some_text = input()
# count_plus = 0
# count_astr = 0
# for i in range(len(some_text)):
#     if some_text[i] == "+":
#         count_plus += 1
#     if some_text[i] == "*":
#         count_astr += 1
# print(f"Символ + встречается {count_plus} раз")
# print(f"Символ * встречается {count_astr} раз")

# some_text = input()
# count = 0
# for i in range(1, len(some_text)):
#     if some_text[i] == some_text[i-1]:
#         count += 1
# print(count)


# some_text = input()
# glassn = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"
# so_glassn = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
# count_glas = 0
# count_sogl = 0
# for i in range(len(some_text)):
#     if some_text[i] in glassn:
#         count_glas += 1

#     if some_text[i] in so_glassn:
#         count_sogl += 1

# print(f"Количество гласных букв равно {count_glas}")
# print(f"Количество согласных букв равно {count_sogl}")
# print(len(some_text))

# x = int(input())
# print(format(x, "b"))

# s = 'abcdefg'
# print(s[2:5])

# s = 'abcdefg'
# print(s[3:])

# s = 'abcdefg'
# print(s[:3])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# s = input()
# s2 = s[::-1]

# if s == s2:
#     print("YES")
# else:
#     print("NO")

# s = input()
# print(len(s))
# print(s*3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:len(s)-1])


# s = input()
# print(s[2])
# print(s[len(s)-2])
# print(s[:5])
# print(s[:len(s)-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-1::-2])

# s = input()
# s1 = s[:len(s)//2 + len(s) % 2]
# s2 = s[len(s)//2 + len(s) % 2:]
# print(s2+s1)

# s = 'i Learn Python language'
# print(s.capitalize())

# s = 'i LEARN Python LAnguaGE'
# print(s.lower())

# s = '$12344%^$#@!'
# print(s.lower())

# s1 = 'a'
# s2 = s1.upper()
# print(s1, s2)

# s = 'i LEARN Python LAnguaGE'
# print(s.upper())

# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())

# s = input()
# s2 = s.title()
# if s == s2:
#     print("YES")
# else:
#     print("NO")

# s = input()
# print(s.swapcase())

# s = input()
# is_good = "хорош" in s.lower()
# if is_good:
#     print("YES")
# else:
#     print("NO")

# s = input()
# s_upper = s.upper()
# count = 0
# for i in range(len(s)):
#     if s[i] != s_upper[i]:
#         count += 1

# print(count)
##################################################################################################
# • isalpha(str): если строка в Python включает в себя лишь алфавитные символы, возвращается True;

# • islower(str): True возвращается, если строка включает лишь символы в нижнем регистре;

# • isupper(str): True, если символы строки в Python находятся в верхнем регистре;

# • startswith(str): True, когда строка начинается с подстроки str;

# • isdigit(str): True, когда каждый символ строки — цифра;

# • endswith(str): True, когда строка в Python заканчивается на подстроку str;

# • upper(): строка переводится в верхний регистр;

# • lower(): строка переводится в нижний регистр;

# • title(): для перевода начальных символов всех слов в строке в верхний регистр;

# • capitalize(): для перевода первой буквы самого первого слова строки в верхний регистр;

# • lstrip(): из строки в Python удаляются начальные пробелы; • rstrip(): из строки в Python удаляются конечные пробелы;

# • strip(): из строки в Python удаляются и начальные, и конечные пробелы;

# • rjust(width): когда длина строки меньше, чем параметр width, слева добавляются пробелы, строка выравнивается по правому краю;

# • ljust(width): когда длина строки в Python меньше, чем параметр width, справа от неё добавляются пробелы для дополнения значения width, при этом происходит выравнивание строки по левому краю;

# • find(str[, start[, end]): происходит возвращение индекса подстроки в строку в Python. В том случае, если подстрока не найдена, выполняется возвращение числа - 1;

#        • center(width): когда длина строки в Python меньше, чем параметр width, слева и справа добавляются пробелы(равномерно) для дополнения значения width, причём происходит выравнивание строки по центру;

#        • split([delimeter[, num]]): строку в Python разбиваем на подстроки в зависимости от разделителя;

#        • replace(old, new[, num]): в строке одна подстрока меняется на другую;

#        • join(strs): строки объединяются в одну строку, между ними вставляется определённый разделитель.
############################################################################################################

# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))


# s = 'www.stepik.org'
# print(s.startswith('www'))

# s = 'www.stepik.org'
# print(s.endswith('.ru'))

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))


# s = '     I learn Python language               '
# print(s.strip())

# s = 'abcdababa'
# print(s.replace('ab', '123'))

# s = input()
# print(s.count(" ")+1)

# s = input().lower()

# print("Аденин:", s.count('а'))
# print("Гуанин:", s.count('г'))
# print("Цитозин:", s.count('ц'))
# print("Тимин:", s.count('т'))

# n = int(input())
# count = 0
# for _ in range(n):
#     some_text = input()
#     if some_text.count('11') >= 3:
#         count += 1

# print(count)

# s = input()
# digits = "0123456789"
# count = 0
# for i in range(len(s)):
#     if s[i] in digits:
#         count += 1
# print(count)

# s = input().lower()
# if s.endswith('.com') or s.endswith('.ru'):
#     print("YES")
# else:
#     print("NO")

# s = input()
# max = 0
# max_index = -1

# for i in range(len(s)):
#     cur_count = s.count(s[i])
#     if cur_count >= max:
#         max = cur_count
#         max_index = i

# print(s[max_index])


# s = input()

# if s.count("f") == 1:
#     print(s.index("f"))
# elif s.count("f") > 1:
#     print(s.index("f"), s.rindex("f"))
# else:
#     print("NO")


# s = input()
# first_index = s.index("h")
# last_index = s.rindex("h")
# new_str = s[:first_index] + s[last_index+1:]
# print(new_str)


# s1 = 'abc123'
# s2 = 'abc$*123'
# s3 = ''

# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())

# s1 = 'ABCabc'
# s2 = 'abc123'
# s3 = ''

# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())


# s1 = '1234567'
# s2 = 'abc123'
# s3 = ''

# print(s1.isdigit())
# print(s2.isdigit())
# print(s3.isdigit())

# s1 = 'abc'
# s2 = 'abc1$d'
# s3 = 'Abc1$D'

# print(s1.islower())
# print(s2.islower())
# print(s3.islower())

# s1 = 'ABC'
# s2 = 'ABC1$D'
# s3 = 'Abc1$D'

# print(s1.isupper())
# print(s2.isupper())
# print(s3.isupper())

# s1 = '       '
# s2 = 'abc1$d'

# print(s1.isspace())
# print(s2.isspace())


# s = 'aabbAA111ccDDaa'
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())

# s = 'aabb!@#$11cc'
# print(s.islower())

# s = 'AAb!@#$11CC'
# print(s.isupper())


# s = '    abbc    '
# print(s.isspace())


# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# year = 2010
# sum = "10k"
# curr = "Bitcoin"
# print(s.format(year, sum, curr))


# year = 2010
# amount = '10K'
# currency = 'Bitcoin'

# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# num1 = ord('A')
# num2 = ord('B')
# num3 = ord('a')
# print(num1, num2, num3)

# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(110)
# print(chr1, chr2, chr3)

# for i in range(26):
#     print(chr(ord('A') + i))

# print(ord('foo'))
# a, b = int(input()), int(input())

# for i in range(a, b+1):
#     print(chr(i), end=" ")

# text = input()
# for i in range(len(text)):
#     print(ord(text[i]), end=" ")


# sdvig = int(input())
# text = input()
# for i in range(len(text)):
#     decr = ord(text[i]) - sdvig
#     if decr < 97:
#         decr += 26
#     de_char = chr(decr)
#     print(de_char, end="")

# s = 'Python rocks!'
# print(s[3])
# s = 'Python rocks!'
# print(s[1:6])

# s = '    Python rocks!     '
# print(s.strip())

# s = 'Python rocks!'
# print(s.upper())

# s = 'Python rocks!'
# print(s.replace("o", "@"))

# s = input()
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end="")

# s = input()
# print(s.replace("1", "one"))

# s = input()
# for i in range(len(s)):
#     if s[i] != "@":
#         print(s[i], end="")

# s = input()
# count = 0
# if s.count("f") == 0:
#     print(-2)
# elif s.count("f") == 1:
#     print(-1)
# else:
#     first_index = s.find("f")
#     secon_index = s.find("f", first_index+1)
#     print(secon_index)

# s = input()
# left_index = s.index("h")
# right_index = s.rindex("h")
# s_left = s[:left_index]
# s_middle = s[left_index:right_index+1]
# s_middle_reverse = s_middle[::-1]
# s_right = s[right_index+1:]
# print(s_left+s_middle_reverse + s_right)

# numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
# print(numbers)


# names = ['Michael', 'John', 'Freddie']
# print(names)
