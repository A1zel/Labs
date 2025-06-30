import time
from itertools import combinations, permutations

women = ['W1', 'W2', 'W3']
men = ['M1', 'M2', 'M3']
all_candidates = women + men

# Алгоритмический способ
start = time.time()
results_algo = []

for w in combinations(women, 2):
    left_after_w = [x for x in all_candidates if x not in w]
    for m in combinations([x for x in left_after_w if x in men], 2):
        left_after_m = [x for x in left_after_w if x not in m]
        for l in permutations(left_after_m, 2):
            results_algo.append((w, m, l))
end = time.time()
print(f"Алгоритмический способ: {len(results_algo)} вариантов, время: {end-start:.4f} сек")

# Функциональный способ
start = time.time()
results_func = []

for w in combinations(women, 2):
    rest1 = set(all_candidates) - set(w)
    for m in combinations(rest1 & set(men), 2):
        rest2 = rest1 - set(m)
        for l in permutations(rest2, 2):
            results_func.append((w, m, l))
end = time.time()
print(f"Функциональный способ: {len(results_func)} вариантов, время: {end-start:.4f} сек")

# Оптимизация: поиск лучшего решения с максимальным количеством женщин
best_solution = None
max_women_total = -1
filtered_results = []

for w in combinations(women, 2):
    rest1 = set(all_candidates) - set(w)
    for m in combinations(rest1 & set(men), 2):
        rest2 = rest1 - set(m)
        for l in permutations(rest2, 2):
            if l[0] in women and l[1] in women:
                continue
            total_women = sum(1 for group in [w, m, l] for person in group if person in women)
            if total_women > max_women_total:
                max_women_total = total_women
                best_solution = (w, m, l)
            filtered_results.append((w, m, l))

print(f"Вариантов после ограничения: {len(filtered_results)}")
print(f"Оптимальное решение (максимум женщин): {best_solution}, всего женщин: {max_women_total}")
