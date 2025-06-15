def input_matrix(N):
    print(f"Введите элементы матрицы {N}x{N} построчно через пробел:")
    matrix = []
    for i in range(N):
        while True:
            row_input = input(f"Строка {i + 1}: ").strip()
            row = list(map(int, row_input.split()))
            if len(row) != N:
                print(f"Ошибка: необходимо ввести ровно {N} чисел.")
            else:
                matrix.append(row)
                break
    return matrix

def print_matrix(name, matrix):
    print(f"{name}:")
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

def is_symmetric(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def copy_matrix(matrix):
    return [row[:] for row in matrix]

def add_matrices(A, B):
    N = len(A)
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def subtract_matrices(A, B):
    N = len(A)
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def multiply_matrices(A, B):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sum_ = 0
            for k in range(N):
                sum_ += A[i][k] * B[k][j]
            result[i][j] = sum_
    return result

def transpose(matrix):
    N = len(matrix)
    transposed = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed

def swap_regions(F, A, region='symmetric'):

    N = len(F)

    mid = N // 2

    if region == 'symmetric':
        # Меняем области 1 и 3 симметрично относительно диагонали
        # То есть меняем блоки (0:mid,0:mid) и (mid:N, mid:N) местами с отражением по диагонали
        size_i = mid
        size_j = mid
        for i in range(size_i):
            for j in range(size_j):
                # Меняем F[i][j] и F[mid + j][mid + i]
                F[i][j], F[mid + j][mid + i] = F[mid + j][mid + i], F[i][j]

                # Аналогично для A (если нужно менять в A — уточните)
                # В условии сказано, что А не меняется.

        print("Области 1 и 3 обменены симметрично.")

    else:
        # Нестимметричный обмен областей 1 и 2 несимметрично (по условию)
        size_i = mid
        size_j = mid
        for i in range(size_i):
            for j in range(size_j):
                # Меняем F[i][j] и F[i][j + mid]
                F[i][j], F[i][j + mid] = F[i][j + mid], F[i][j]

        print("Области 1 и 2 обменены несимметрично.")

def main():
    K = float(input("Введите K: "))
    N = int(input("Введите N: "))

    A = input_matrix(N)

    print_matrix("Матрица A", A)

    F = copy_matrix(A)

    print_matrix("Изначальная матрица F", F)

    symmetric_flag = is_symmetric(A)

    if symmetric_flag:
        print("Матрица A симметрична относительно главной диагонали.")
        swap_regions(F, A, region='symmetric')
        print_matrix("Матрица F после обмена (симметричный)", F)
        print("Матрица А не меняется.")
        AT = transpose(A)
        print_matrix("Транспонированная матрица AT", AT)
        FA_sum = add_matrices(F, A)
        print_matrix("F + A", FA_sum)
        FA_sum_K_multiplied = [[K * elem for elem in row] for row in FA_sum]
        print_matrix("K * (F + A)", FA_sum_K_multiplied)
        product1 = multiply_matrices(FA_sum_K_multiplied, AT)
        print_matrix("(K * (F + A)) * AT", product1)
        part2 = subtract_matrices(product1, AT)
        print_matrix("(K * (F + A) * AT) - AT", part2)
        result = add_matrices(part2, F)
        print_matrix("Итоговый результат", result)
if __name__ == "__main__":
    main()