import time


# Функция для вычисления факториала
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


# Функция для вычисления степени числа
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


# Рекурсивная реализация
def recursive_f(n, prev_integral=0):
    if n < 2:
        return 1
    fact_n = factorial(n)
    fact_2n = factorial(2 * n)
    # Используем предыдущее значение интеграла
    return power(-1, n) * (recursive_f(n - 1, prev_integral) / fact_n + recursive_f(n // 5,prev_integral) / fact_2n) + prev_integral


# Итеративная реализация
def iterative_f(n):
    if n < 2:
        return 1

    # Создаем список для хранения промежуточных значений
    results = [0] * (n + 1)
    results[0] = 1  # Базовый случай
    prev_integral = 0  # Предыдущее значение интеграла

    for i in range(1, n + 1):
        fact_i = factorial(i)
        fact_2i = factorial(2 * i)

        # Вычисляем значение с учетом предыдущих результатов и интеграла
        term1 = results[i - 1] / fact_i
        term2 = results[i // 5] / fact_2i
        results[i] = power(-1, i) * (term1 + term2) + prev_integral
        prev_integral = results[i]  # Обновляем предыдущее значение интеграла

    return results[n]


# Функция для измерения времени выполнения
def measure_time(func, n):
    start_time = time.perf_counter()
    try:
        result = func(n)
        end_time = time.perf_counter()
        return end_time - start_time, result
    except RecursionError:
        return float('inf'), None


# Тестирование и сравнение
test_values = [1, 2, 3, 5, 10, 15, 20]
results = []

for n in test_values:
    rec_time, rec_result = measure_time(lambda x: recursive_f(x, 0), n)
    iter_time, iter_result = measure_time(iterative_f, n)

    results.append([
        n,
        rec_result,
        f"{rec_time:.6f} сек",
        iter_result,
        f"{iter_time:.6f} сек"
    ])

# Вывод результатов в табличной форме
print("Результаты сравнения методов:")
print(f"{'n':<5}{'Рекурсивный':<15}{'Время рекурсии':<15}{'Итеративный':<15}{'Время итерации':<15}")
print("-" * 75)
for row in results:
    print(f"{row[0]:<5}{row[1]:<15.6f}{row[2]:<15}{row[3]:<15.6f}{row[4]:<15}")

# Анализ границ применимости
print("\nАнализ границ применимости:")
print("Рекурсивный метод ограничен:")
print("- Глубиной рекурсии (обычно около 1000 уровней)")
print("- Временем вычисления факториалов")
print("- Памятью стека")

print("\nИтеративный метод ограничен:")
print("- Доступной памятью для хранения промежуточных результатов")
print("- Временем вычисления, но оно значительно меньше рекурсивного")
print("- Эффективен для больших значений n")
