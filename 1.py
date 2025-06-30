print('Введите K:', end=' ')
K = int(input())
print('Введите N:', end=' ')
N = int(input())

# Чтение матрицы из файла matrix.txt и проверка на N
with open('matrix.txt', 'r') as file:
    A = []
    for line in file:
        row = list(map(int, line.strip().split()))
        # Проверка на количество столбцов = N
        if len(row) != N:
            print('Значение N не равно количеству столбцов в матрице')
            exit()
        A.append(row)
    # Проверка на количество строк = N
    if len(A) != N:
        print('Значение N не равно количеству строк в матрице')
        exit()

# Вывод матрицы А
print("\nМатрица A:")
for row in A:
    print(row)

# Анализ матрицы по областям
area_1 = []  # Ниже гл. диагонали и выше побочной
area_2 = []  # Выше гл. диагонали и выше побочной
area_3 = []  # Выше гл. диагонали и ниже побочной
area_4 = []  # Ниже гл. диагонали и ниже побочной
matrix = []  # Область 1 в виде подматрицы для проверки симметрии относительно медианы
for i in range(N):
    # Временный список для текущей строки области 1
    row_area_1 = []
    # Главная диагональ: i = j
    # Побочная диагональ: j = N - (i + 1)
    for j in range(N):
        # область 1
        if i > j and j < N - (i + 1):
            area_1.append(A[i][j])
            row_area_1.append(A[i][j])
        # область 2
        elif i < j and j < N - (i + 1):
            area_2.append(A[i][j])
        # область 3
        elif i < j and j > N - (i + 1):
            area_3.append(A[i][j])
        # область 4
        elif i > j and j > N - (i + 1):
            area_4.append(A[i][j])
    if row_area_1:  # Не добавляем пустые строки
        matrix.append(row_area_1.copy())

# Вывод результатов
print("\nОбласти матрицы:")
print("Область 1:", area_1)
print("Область 2:", area_2)
print("Область 3:", area_3)
print("Область 4:", area_4)

# Создаётся копия исходной матрицы A в новую переменную F, чтобы изменения происходили только с копией
F = A.copy()

# Проверка симметричности области 1 относительно медианы
is_symmetric = True
n = len(matrix)
for i in range(n // 2):
    row1 = matrix[i]
    row2 = matrix[n - 1 - i]
    # Поэлементное сравнение
    for a, b in zip(row1, row2):
        if a != b:
            is_symmetric = False

# Выводится результат проверки симметрии
if is_symmetric == True:
    print("\nОбласть 1 симметрична относительно медианы")
    # Меняем местами элементы областей 2 и 4 поэлементно
    for i in range(N):
        for j in range(N):
            if i < j and j < N - i - 1:  # область 2
                x, y = N - i - 1, j      # симметричная точка в области 4
                F[i][j], F[x][y] = F[x][y], F[i][j]
else:
    print("\nОбласть 1 не симметрична относительно медианы")
    # Области 1 и 2 меняются местами не симметрично, без учёта позиций
    idx1 = 0
    idx2 = 0
    for i in range(N):
        for j in range(N):
            if i > j and j < N - i - 1:
                F[i][j] = area_2[idx1]
                idx1 += 1
            elif i < j and j < N - i - 1:
                F[i][j] = area_1[idx2]
                idx2 += 1

# Вывод изменённой матрицы F
print("\nМатрица F:")
for row in F:
    print(row)

# Транспонирование матрицы A
A_T = []
for i in range(N):
    new_row = []
    for j in range(N):
        new_row.append(A[j][i])
    A_T.append(new_row)
print("\nМатрица A^T:")
for row in A_T:
    print(row)

# Умножение A на A^T
A_AT = [[0]*N for _ in range(N)]
for i in range(N):
    for k in range(N):
        if A[i][k] != 0:
            for j in range(N):
                A_AT[i][j] += A[i][k] * A_T[k][j]
print("\nМатрица A * A^T:")
for row in A_AT:
    print(row)

# Сложение A^T и F
AT_plus_F = [[A_T[i][j] + F[i][j] for j in range(N)] for i in range(N)]
print("\nМатрица A^T + F:")
for row in AT_plus_F:
    print(row)

# Умножение A^T + F на K
K_AT_plus_F = [[K * AT_plus_F[i][j] for j in range(N)] for i in range(N)]
print("\nМатрица K * (A^T + F):")
for row in K_AT_plus_F:
    print(row)

# Вычитание: A * A^T - K * (A^T + F)
result = [[A_AT[i][j] - K_AT_plus_F[i][j] for j in range(N)] for i in range(N)]
print("\nРезультат: A * A^T - K * (A^T + F):")
for row in result:
    print(row)