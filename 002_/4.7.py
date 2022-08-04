# 6 #########################
# Найти произведение матриц
#
#
# n1, m1 = [int(item) for item in input().split()]
# n2, m2 = [int(item) for item in input().split()]


# matrix_A = []
# matrix_B = []
# matrix_C = []

# for i in range(n1):
#     matrix_C.append([0]*m2)

# for i in range(n1):
#     matrix_A.append([int(item) for item in input().split()])
# print()

# for i in range(n2):
#     matrix_B.append([int(item) for item in input().split()])
# print()
# # iterate through rows of matrix_A
# for i in range(len(matrix_A)):
#     # iterate through columns of matrix_B
#     for j in range(len(matrix_B[0])):
#         # iterate through rows of matrix_B
#         for k in range(len(matrix_B)):
#             matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]

# for i in range(n1):
#     for j in range(m2):
#         print(str(matrix_C[i][j]).ljust(3), end=' ')
#     print()


######################################################
# 8 #########################
# Найти произведение матриц 25 раз
#
#

def mult_matrix(matrix_A, matrix_B):
    matrix_result = []
    for i in range(len(matrix_A)):
        matrix_result.append([0]*len(matrix_B[0]))

    # iterate through rows of matrix_A
    for i in range(len(matrix_A)):
        # iterate through columns of matrix_B
        for j in range(len(matrix_B[0])):
            # iterate through rows of matrix_B
            for k in range(len(matrix_B)):
                matrix_result[i][j] += matrix_A[i][k] * matrix_B[k][j]
    return matrix_result


n, m = [int(item) for item in input().split()]
stepen = int(input())

matrix_A = []
matrix_C = []

for i in range(n):
    row = [int(item) for item in input().split()]
    matrix_A.append(row)
    matrix_C.append(row)
print()

for i in range(stepen-1):
    matrix_C = mult_matrix(matrix_C, matrix_A)

for i in range(n):
    for j in range(m):
        print(str(matrix_C[i][j]).ljust(3), end=' ')
    print()


######################################################
