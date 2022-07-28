# 1 #########################
# Таблица умножения
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

# rows, cols = int(input()), int(input())
# my_matrix = []
# for i in range(rows):
#     my_matrix.append([0]*cols)

# for i in range(rows):
#     for j in range(cols):
#         my_matrix[i][j] = i * j
#         print(str(my_matrix[i][j]).ljust(3), end='')
#     print()


######################################################
# 2 #########################
# Максимум в таблице
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем nn строк по mm целых чисел в каждой, отделенных символом пробела.Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.
# rows, cols = int(input()), int(input())
# my_matrix = []
# max = -10**6
# for i in range(rows):
#     my_matrix.append([int(item) for item in input().split()])

# for i in range(rows):
#     for j in range(cols):
#         if my_matrix[i][j] > max:
#             max = my_matrix[i][j]
# flag = True
# for i in range(rows):
#     for j in range(cols):
#         if my_matrix[i][j] == max and flag:
#             print(f"{i} {j}")
#             flag = False
######################################################
# 3 #########################
# Обмен столбцов
# Напишите программу, которая меняет местами столбцы в матрице.
# На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.
# rows, cols = int(input()), int(input())
# my_matrix = []
# for i in range(rows):
#     my_matrix.append([int(item) for item in input().split()])

# coulumn_to_swap = [int(item) for item in input().split()]
# k = coulumn_to_swap[0]
# m = coulumn_to_swap[1]
# for i in range(rows):
#     my_matrix[i][k], my_matrix[i][m] = my_matrix[i][m], my_matrix[i][k]
#     print(*my_matrix[i])
######################################################
# 4 #########################
# Симметричная матрица
# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
# n = int(input())

# is_simetr = True
# my_matrix = []
# for i in range(n):
#     my_matrix.append([int(item) for item in input().split()])

# for i in range(n):
#     for j in range(n):
#         if my_matrix[i][j] == my_matrix[j][i] and is_simetr:
#             is_simetr = True
#         else:
#             is_simetr = False
# if is_simetr:
#     print("YES")
# else:
#     print("NO")


######################################################
# 5 #########################
# Обмен диагоналей
# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
# n = int(input())
# my_matrix = []
# for i in range(n):
#     my_matrix.append([int(item) for item in input().split()])

# for i in range(n):
#     my_matrix[i][i], my_matrix[n-1-i][i] = my_matrix[n-1-i][i], my_matrix[i][i]


# for i in range(n):
#     print(*my_matrix[i])

######################################################
# 6 #########################
# Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
# n = int(input())
# my_matrix = []
# for i in range(n):
#     my_matrix.append([int(item) for item in input().split()])

# my_matrix.reverse()

# for i in range(n):
#     print(*my_matrix[i])


######################################################
# 7 #########################
# Поворот матрицы
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

# n = int(input())
# my_matrix = []
# for i in range(n):
#     my_matrix.append([int(item) for item in input().split()])


# for col in range(n):
#     for row in range(n-1, -1, -1):
#         print(my_matrix[row][col], end=" ")
#     print()


######################################################
# 8 #########################
# Ходы коня
# На шахматной доске 8 \times 88×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.
# На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 11 до 88, снизу вверх)).
# coord = input()
# list_cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# list_rows = ['1', '2', '3', '4', '5', '6', '7', '8']
# list_rows.reverse()
# my_matrix = []
# for i in range(8):
#     my_matrix.append(["."]*8)
# horse_row = list_rows.index(coord[1])
# horse_col = list_cols.index(coord[0])

# for i in range(8):
#     for j in range(8):
#         if i == horse_row and j == horse_col:
#             my_matrix[i][j] = "N"
#         elif (abs(i-horse_row) == 1 and abs(j-horse_col) == 2) or (abs(i-horse_row) == 2 and abs(j-horse_col) == 1):
#             my_matrix[i][j] = "*"
#         else:
#             continue


# for i in range(8):
#     print(*my_matrix[i])
######################################################
# 9 #########################
# Магический квадрат 🌶️
# Магическим квадратом порядка n называется квадратная таблица размера nxn, составленная из всех чисел 1, 2, 3, ...,n**2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

n = int(input())
my_matrix = []
plane_list = []
for i in range(n):
    new_row = [int(item) for item in input().split()]
    my_matrix.append(new_row)
    plane_list.extend(new_row)
is_all_numbers_in = True
numbers_list = [item for item in range(1, n**2+1)]

for item in numbers_list:
    if item not in plane_list:
        is_all_numbers_in = False
        break

if not is_all_numbers_in:
    print("NO")

else:
    control_sum = sum(my_matrix[0])
    is_rows = True
    is_column = True

    for i in range(n):
        if sum(my_matrix[i]) == control_sum and is_rows:
            continue
        else:
            is_rows = False
            break

    for col in range(n):
        sum_col = 0
        for row in range(n):
            sum_col += my_matrix[row][col]

        if sum_col != control_sum or not is_column:
            is_column = False
            break
        else:
            continue

    sum_main_diag = 0
    sum_other_diag = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                sum_main_diag += my_matrix[i][j]

            if j+i == n-1:
                sum_other_diag += my_matrix[i][j]

    if (sum_main_diag == sum_other_diag == control_sum) and is_rows and is_column:
        print("YES")
    else:
        print("NO")


######################################################
