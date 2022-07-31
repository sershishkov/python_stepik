# 1 #########################
# Шахматная доска
# На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n \times mn×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.
# На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
# matrix_size = [int(item) for item in input().split()]
# n = matrix_size[0]
# m = matrix_size[1]
# my_matrix = []
# for i in range(n):
#     my_matrix.append(["."]*m)

# for i in range(n):
#     for j in range(m):
#         if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
#             my_matrix[i][j] = "*"


# for i in range(n):
#     print(*my_matrix[i])
######################################################
# 2 #########################
# Побочная диагональ
# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:
# числа на побочной диагонали равны 11
# числа, стоящие выше этой диагонали, равны 00
# числа, стоящие ниже этой диагонали, равны 22.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.
#
# n = int(input())
# my_matrix = []
# for i in range(n):
#     my_matrix.append(["0"]*n)

# for i in range(n):
#     for j in range(n):
#         if i + j == n - 1:
#             my_matrix[i][j] = "1"
#         if i + j >= n:
#             my_matrix[i][j] = "2"

# for i in range(n):
#     print(*my_matrix[i])
######################################################
# 3 #########################
# Заполнение 1
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m и заполняет её числами от 11 до n \cdot mn⋅m в соответствии с образцом.
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

# matrix_size = [int(item) for item in input().split()]
# n = matrix_size[0]
# m = matrix_size[1]
# my_matrix = []
# numbers_list = [item for item in range(1, n*m+1)]
# for i in range(n):
#     my_matrix.append(numbers_list[i*m:i*m+m])

# for i in range(n):
#     for j in range(m):
#         print(str(my_matrix[i][j]).ljust(2), end=' ')
#     print()

######################################################
# 4 #########################
# Заполнение 2
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m заполнив её в соответствии с образцом.
# matrix_size = [int(item) for item in input().split()]
# n = matrix_size[1]
# m = matrix_size[0]
# my_matrix = []
# numbers_list = [item for item in range(1, n*m+1)]
# for i in range(n):
#     my_matrix.append(numbers_list[i*m:i*m+m])

# for i in range(m):
#     for j in range(n):
#         print(str(my_matrix[j][i]).ljust(3), end=' ')
#     print()

######################################################
# 5 #########################
# Заполнение 3
# Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
#
# n = int(input())
# my_matrix = []
# for i in range(n):
#     my_matrix.append(["0"]*n)

# for i in range(n):
#     for j in range(n):
#         if (i == j) or (i+j == n-1):
#             my_matrix[i][j] = 1

# for i in range(n):
#     for j in range(n):
#         print(str(my_matrix[i][j]).ljust(3), end=' ')
#     print()

######################################################
# 6 #########################
# Заполнение 4
# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n заполнив её в соответствии с образцом.
#
# n = int(input())
# my_matrix = []
# for i in range(n):
#     my_matrix.append(["0"]*n)

# for i in range(n):
#     for j in range(n):
#         if (i < j and i < n-1-j) or (i > j and i > n-1-j) or (i == j) or (i+j == n-1):
#             my_matrix[i][j] = 1

# for i in range(n):
#     for j in range(n):
#         print(str(my_matrix[i][j]).ljust(3), end=' ')
#     print()

######################################################
# 7 #########################
# Заполнение 5 🌶️
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m заполнив её в соответствии с образцом.
#
# matrix_size = [int(item) for item in input().split()]
# n = matrix_size[0]
# m = matrix_size[1]
# row = [i for i in range(1, m+1)]

# my_matrix = []
# for i in range(n):
#     my_matrix.append(row)
#     row = row[1:]+row[0:1]

# for i in range(n):
#     for j in range(m):
#         print(str(my_matrix[i][j]).ljust(3), end=' ')
#     print()


######################################################
# 8 #########################
# Заполнение змейкой
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m заполнив её "змейкой" в соответствии с образцом.
#
# matrix_size = [int(item) for item in input().split()]
# n = matrix_size[0]
# m = matrix_size[1]
# digit_list = [i for i in range(1, n*m+1)]

# my_matrix = []
# row = []
# for i in range(n):
#     if i % 2 == 1:
#         row = digit_list[i*m:i*m+m]
#         row = row[::-1]
#     else:
#         row = digit_list[i*m:i*m+m]

#     my_matrix.append(row)

# for i in range(n):
#     for j in range(m):
#         print(str(my_matrix[i][j]).ljust(3), end=' ')
#     print()

######################################################
# 9 #########################
# Заполнение диагоналями 🌶️
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m заполнив её "диагоналями" в соответствии с образцом.
#
# matrix_size = [int(item) for item in input().split()]
# n = matrix_size[0]
# m = matrix_size[1]


# my_matrix = []
# for i in range(n):
#     for j in range(m):
#         my_matrix.append([0]*m)
# current_number = 1

# for j in range(n + m - 1):
#     for i in range(n):
#         if j - i in range(m):
#             my_matrix[i][j-i] = current_number
#             current_number += 1


# for i in range(n):
#     for j in range(m):
#         print(str(my_matrix[i][j]).ljust(3), end=' ')
#     print()

######################################################
# 10 #########################
# Заполнение спиралью 😈😈
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

def change_direction(old_direction):
    directions = ['right', 'down', 'left',  'up']
    index = directions.index(old_direction)
    if index == 3:
        return directions[0]
    else:
        return directions[index+1]


n, m = [int(item) for item in input().split()]
my_matrix = []
for i in range(n):
    for j in range(m):
        my_matrix.append([0]*m)

count_r = 0
count_d = 0
count_l = 0
count_u = 0

i, j = 0, 0
current_direction = 'right'
if m == 1:
    for i in range(1, n+1):
        print(i)
else:
    for k in range(1, n*m+1):
        my_matrix[i][j] = k
        # print(f"k={k} my_matrix[{i}][{j}]={my_matrix[i][j]}")

        if current_direction == 'right':
            if 0 <= j+1 < m-1 and (my_matrix[i][j+1] == 0):
                j += 1
            else:
                if count_r == 0:
                    j += 1
                    count_r += 1
                if my_matrix[i][j] > 0:
                    i += 1
                current_direction = change_direction(current_direction)

        elif current_direction == 'down':
            if 0 <= i+1 < n-1 and (my_matrix[i+1][j] == 0):
                i += 1
            else:
                if count_d == 0:
                    i += 1
                    count_d += 1
                if my_matrix[i][j] > 0:
                    j -= 1
                current_direction = change_direction(current_direction)

        elif current_direction == 'left':
            if m > j-1 >= 1 and (my_matrix[i][j-1] == 0):
                j -= 1
            else:
                if count_l == 0:
                    j -= 1
                    count_l += 1
                if my_matrix[i][j] > 0:
                    i -= 1
                current_direction = change_direction(current_direction)

        elif current_direction == 'up':
            if n > i-1 >= 1 and (my_matrix[i-1][j] == 0):
                i -= 1
            else:
                if count_u == 0:
                    j += 1
                    count_u += 1
                if my_matrix[i][j] > 0:
                    j += 1
                current_direction = change_direction(current_direction)

    for i in range(n):
        for j in range(m):
            print(str(my_matrix[i][j]).ljust(3), end=' ')
        print()


######################################################
