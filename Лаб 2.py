import numpy as np
import matplotlib.pyplot as plt

def input_parameters():
    K = float(input("Введите K: "))
    N = int(input("Введите N (кратное 2): "))
    if N % 2 != 0:
        raise ValueError("N должно быть четным числом.")
    return K, N

def create_submatrices(N):
    half = N // 2
    print(f"Введите элементы для подматриц B, C, D, E размером {half}x{half}:")
    print("Для удобства можно использовать фиксированные значения или считать из файла.")

    B = np.array([[i for i in range(half)] for _ in range(half)])
    C = np.array([[i + 10 for i in range(half)] for _ in range(half)])
    D = np.array([[i + 20 for i in range(half)] for _ in range(half)])
    E = np.array([[i + 30 for i in range(half)] for _ in range(half)])

    return B, C, D, E

def assemble_matrix(N, B, C, D, E):
    top = np.hstack((B, E))
    bottom = np.hstack((C, D))
    A = np.vstack((top, bottom))
    return A

def is_symmetric(matrix):
    return np.allclose(matrix, matrix.T)

def form_F(A):
    F = A.copy()
    n = A.shape[0] // 2
    B = F[:n, :n]
    C = F[n:, :n]
    E = F[:n, n:]

    if is_symmetric(F):
        # Меняем местами B и C симметрично
        F[:n, :n], F[n:, :n] = C.copy(), B.copy()
        print("Матрица симметрична: поменяли местами B и C.")
    else:
        # Меняем местами C и E несимметрично
        F[n:, :n], F[:n, n:] = E.copy(), C.copy()
        print("Матрица несимметрична: поменяли местами C и E.")

    return F

def main():
    K, N = input_parameters()

    B, C, D, E = create_submatrices(N)

    A = assemble_matrix(N, B, C, D, E)

    print("\nМатрица А:")
    print(A)
    F = form_F(A)
    print("\nМатрица F после перестановок:")
    print(F)

def compute_and_plot(K, A, F):
    detA = np.linalg.det(A)
    sum_diag_F = np.trace(F)
    print(f"\nОпределитель A: {detA}")
    print(f"Сумма диагональных элементов F: {sum_diag_F}")

    G = np.tril(A)  # Нижняя треугольная матрица G
    print("\nНижняя треугольная матрица G из A:")
    print(G)

    if detA > sum_diag_F:
        try:
            invA = np.linalg.inv(A)
            invF = np.linalg.inv(F)
            AT = A.T
            expr1 = invA @ AT - K * invF
            print("\nВычисляем выражение: invA * AT - K * invF")
            print(expr1)
            result_for_graphs = expr1
            title_for_graphs = ["invA * AT - K * invF"]
        except np.linalg.LinAlgError:
            print("Одна из матриц не является обратимой.")
            result_for_graphs = None
            title_for_graphs = []
    else:
        try:
            invA_plus_G_minus_FT = (np.linalg.inv(A) + G - F.T) * K
            print("\nВычисляем выражение: (invA + G - F.T)*K")
            print(invA_plus_G_minus_FT)
            result_for_graphs = invA_plus_G_minus_FT
            title_for_graphs = ["(invA + G - F.T)*K"]
        except np.linalg.LinAlgError:
            print("Одна из матриц не является обратимой.")
            result_for_graphs = None
            title_for_graphs = []
    return result_for_graphs, title_for_graphs

def plot_graphs(results, titles):
    plt.figure(figsize=(15, len(results) * 3))
    for idx, (data, title) in enumerate(zip(results, titles)):
        plt.subplot(len(results), 1, idx + 1)
        plt.imshow(data if data.ndim == 2 else data.real, cmap='viridis', aspect='auto')
        plt.colorbar()
        plt.title(title)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()