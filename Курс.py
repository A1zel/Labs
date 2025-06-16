import tkinter as tk
from tkinter import ttk, scrolledtext
import time


# --- Алгоритмическая реализация без itertools ---
def generate_manual(women, men):
    results = []
    for i in range(len(women)):
        for j in range(i + 1, len(women)):
            spec1 = [women[i], women[j]]
            rest_w = [w for w in women if w not in spec1]
            for m in range(len(men)):
                for n in range(m + 1, len(men)):
                    spec2 = [men[m], men[n]]
                    rest_m = [mm for mm in men if mm not in spec2]
                    rest = rest_w + rest_m
                    if len(rest) == 2:
                        spec3 = rest
                        results.append((spec1, spec2, spec3))
    return results


# --- Реализация с itertools ---
def generate_itertools(women, men):
    from itertools import combinations
    all_people = women + men
    results = []
    for spec1 in combinations(women, 2):
        left_after_women = set(all_people) - set(spec1)
        left_men = set(men) & left_after_women
        for spec2 in combinations(left_men, 2):
            left_after_both = left_after_women - set(spec2)
            if len(left_after_both) == 2:
                spec3 = tuple(left_after_both)
                results.append((spec1, spec2, spec3))
    return results


# --- Ограничение: не две женщины на третьей спец ---
def apply_constraint(results):
    filtered = []
    for s1, s2, s3 in results:
        if sum(1 for x in s3 if x.startswith('W')) < 2:
            filtered.append((s1, s2, s3))
    return filtered


# --- Метрика: максимальное число женщин во всех спец ---
def best_by_metric(results):
    max_women = -1
    best_combo = None
    for s1, s2, s3 in results:
        count_women = sum(1 for x in s1 + s2 + s3 if x.startswith('W'))
        if count_women > max_women:
            max_women = count_women
            best_combo = (s1, s2, s3, count_women)
    return best_combo


# --- GUI ---
def run():
    result_text.delete(1.0, tk.END)

    women_count = int(entry_w.get())
    men_count = int(entry_m.get())

    women = [f"W{i + 1}" for i in range(women_count)]
    men = [f"M{i + 1}" for i in range(men_count)]

    # Алгоритмически
    t0 = time.time()
    manual_results = generate_manual(women, men)
    t_manual = (time.time() - t0) * 1000

    # Итератулс
    t0 = time.time()
    itertools_results = generate_itertools(women, men)
    t_itertools = (time.time() - t0) * 1000

    # Сравнение результатов до ограничения
    result_text.insert(tk.END, f"Алгоритмически: {len(manual_results)} вариантов за {t_manual:.4f} мс\n")
    result_text.insert(tk.END, f"itertools:      {len(itertools_results)} вариантов за {t_itertools:.4f} мс\n\n")

    # Ограничение — не две женщины на третьей спец.
    manual_filtered = apply_constraint(manual_results)

    result_text.insert(tk.END, f"После ограничения:\n")
    result_text.insert(tk.END, f"Алгоритмически: {len(manual_filtered)} вариантов\n\n")

    # Метрика — максимум женщин во всех спец.
    best = best_by_metric(manual_filtered)

    # Выводим первые несколько вариантов для примера:
    result_text.insert(tk.END, "Примеры вариантов:\n")

    for idx, (s1, s2, s3) in enumerate(manual_filtered[:10], start=1):
        result_text.insert(tk.END,
                           f"{idx}. Спец1:{s1}, Спец2:{s2}, Спец3:{s3}\n"
                           )

    if best:
        var_best.set(f"Лучший вариант:\nСпец1:{best[0]}, Спец2:{best[1]}, Спец3:{best[2]} | Женщин всего: {best[3]}")


root = tk.Tk()
root.title("Комбинаторные алгоритмы")

frame = ttk.Frame(root);
frame.pack(padx=10, pady=5)

ttk.Label(frame, text="Женщин:").grid(row=0, column=0);
entry_w = ttk.Entry(frame, width=5);
entry_w.insert(0, "3");
entry_w.grid(row=0, column=1)
ttk.Label(frame, text="Мужчин:").grid(row=0, column=2);
entry_m = ttk.Entry(frame, width=5);
entry_m.insert(0, "3");
entry_m.grid(row=0, column=3)

btn_run = ttk.Button(frame, text="Запустить", command=run);
btn_run.grid(row=0, column=4, padx=(10, 0))

var_best = tk.StringVar()
ttk.Label(root, textvariable=var_best, font=("Arial", 12, "bold")).pack(pady=(5, 0))

result_text = scrolledtext.ScrolledText(root, width=80, height=20, font=("Consolas", 10));
result_text.pack(padx=10, pady=(5, 10))

root.mainloop()