# 1 #########################
# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
# count_points = int(input())
# count_1 = 0
# count_2 = 0
# count_3 = 0
# count_4 = 0
# for i in range(count_points):
#     point = input().split(" ")
#     x = int(point[0])
#     y = int(point[1])
#     if x > 0 and y > 0:
#         count_1 += 1
#     elif x < 0 and y > 0:
#         count_2 += 1
#     elif x < 0 and y < 0:
#         count_3 += 1
#     elif x > 0 and y < 0:
#         count_4 += 1

# print(f"Первая четверть: {count_1}")
# print(f"Вторая четверть: {count_2}")
# print(f"Третья четверть: {count_3}")
# print(f"Четвертая четверть: {count_4}")


########################################

# 2 #########################
# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом.
# list_numbers = input().split(" ")
# count = 0
# for i in range(1, len(list_numbers)):
#     if int(list_numbers[i]) > int(list_numbers[i-1]):
#         count += 1
# print(count)

########################################

# 3 #########################
# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу, которая меняет местами соседние элементы списка(a[0] c a[1], a[2] c a[3] и т.д.). Если в списке нечетное количество элементов, то последний остается на своем месте.
# list_numbers = input().split(" ")
# for i in range(1, len(list_numbers), 2):
#     list_numbers[i-1], list_numbers[i] = list_numbers[i], list_numbers[i-1]
# print(*list_numbers)
########################################

# 4 #########################
# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
# list_numbers = [int(item) for item in input().split(" ")]
# list_numbers.insert(0, list_numbers[len(list_numbers)-1])
# list_numbers = list_numbers[:len(list_numbers)-1]
# print(*list_numbers)

########################################

# 5 #########################
# На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.
# list_numbers = [int(item) for item in input().split(" ")]
# count = 1
# for i in range(1, len(list_numbers)):
#     if list_numbers[i] > list_numbers[i-1]:
#         count += 1
# print(count)
########################################

# 6 #########################
# Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат в виде ответа «ДА» или «НЕТ».
# count_numbers = int(input())
# number_list = []
# for i in range(count_numbers):
#     number_list.append(int(input()))

# control_number = int(input())
# is_mult = False
# for i in range(len(number_list)):
#     for j in range(i+1, len(number_list)):
#         if number_list[i]*number_list[j] == control_number:
#             is_mult = True
#             break
# if is_mult:
#     print("ДА")
# else:
#     print("НЕТ")


########################################

# 7 #########################
# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.
# choice_timur = input()
# choice_ruslan = input()

# if choice_timur == choice_ruslan:
#     print("ничья")
# elif (choice_timur == 'камень' and choice_ruslan == 'ножницы') or (choice_timur == 'ножницы' and choice_ruslan == 'бумага') or (choice_timur == 'бумага' and choice_ruslan == 'камень'):
#     print("Тимур")
# else:
#     print("Руслан")


########################################

# 8 #########################
# Проиграв 1010 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.
# choice_timur = input()
# choice_ruslan = input()

# if choice_timur == choice_ruslan:
#     print("ничья")
# elif (choice_timur == 'камень' and (choice_ruslan == 'ножницы' or choice_ruslan == 'ящерица')) or (choice_timur == 'ножницы' and (choice_ruslan == 'бумага' or choice_ruslan == 'ящерица')) or (choice_timur == 'бумага' and (choice_ruslan == 'камень' or choice_ruslan == 'Спок')) or (choice_timur == 'Спок' and (choice_ruslan == 'камень' or choice_ruslan == 'ножницы')) or (choice_timur == 'ящерица' and (choice_ruslan == 'Спок' or choice_ruslan == 'бумага')):
#     print("Тимур")
# else:
#     print("Руслан")

########################################

# 9 #########################
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# my_list = input().split("О")
# max = 0
# for i in range(len(my_list)):
#     if len(my_list[i]) > max:
#         max = len(my_list[i])
# print(max)
########################################

# 10 #########################
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы


# def find_anton(sentence):
#     my_anton = "anton"
#     new_anton = ''
#     start_index = 0
#     for item in my_anton:
#         current_index = sentence.find(item, start_index)
#         if current_index > -1:
#             new_anton += item
#             start_index = current_index + 1
#     return my_anton == new_anton


# count_frig = int(input())
# list_good_frig = []
# for i in range(1, count_frig+1):
#     if find_anton(input()):
#         list_good_frig.append(i)

# print(*list_good_frig)


########################################

# 11 #########################
# Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста, а очередную строку отображает уже без этой буквы.

alphabet_rus = [chr(i) for i in range(1072, 1104)]


def del_letter_from_sentence(sentence, letter):
    new_str = sentence.replace(letter, "")
    new_str = ' '.join(new_str.split())
    return new_str


def find_letter_to_delete(frase):
    first_letter = ''
    for i in range(len(alphabet_rus)):
        if alphabet_rus[i] in frase:
            first_letter = alphabet_rus[i]
            break
    return first_letter


word = input() + ' запретил букву'
new_word = word
prev_letter = find_letter_to_delete(word)
print(word, prev_letter)
for i in range(1, len(alphabet_rus)):
    if len(new_word) < 1:
        break
    elif alphabet_rus[i-1] in new_word:
        new_word = del_letter_from_sentence(new_word, prev_letter)
        prev_letter = find_letter_to_delete(new_word)
        if len(new_word) > 1:
            print(new_word, prev_letter)
        elif len(new_word) == 1:
            print(new_word, new_word)

    else:
        continue


########################################
