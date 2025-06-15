import math
import time
from functools import lru_cache

# Рекурсивная реализация с мемоизацией
@lru_cache(maxsize=None)
def F_recursive(n):
    if n < 2:
        return 1.0
    return ((-1)**n) * (F_recursive(n-1)/math.factorial(n) + F_recursive(n//5)/math.factorial(2*n))

# Итерационная реализация
def F_iterative(n):
    F = [1.0] * (max(2, n+1))
    for i in range(2, n+1):
        F[i] = ((-1)**i) * (F[i-1]/math.factorial(i) + F[i//5]/math.factorial(2*i))
    return F[n]

# Сравнение времени выполнения
print(f"{'n':>3} | {'Rec (ms)':>10} | {'Iter (ms)':>10}")
print('-'*30)
for n in [5, 10, 15, 20, 25, 30]:
    start = time.time()
    res_rec = F_recursive(n)
    t_rec = (time.time() - start)*1000

    start = time.time()
    res_iter = F_iterative(n)
    t_iter = (time.time() - start)*1000

    print(f"{n:>3} | {t_rec:10.3f} | {t_iter:10.3f}")