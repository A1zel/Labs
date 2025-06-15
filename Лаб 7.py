import tkinter as tk
from tkinter import ttk, scrolledtext
from itertools import combinations, permutations

def solve():
    try:
        n_women = int(entry_women.get())
        n_men = int(entry_men.get())
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Введите корректные числа!")
        return

    women = [f"W{i+1}" for i in range(n_women)]
    men = [f"M{i+1}" for i in range(n_men)]
    all_candidates = women + men

    results = []
    max_women_total = -1
    best_solution = None

    for w in combinations(women, 2):
        rest1 = set(all_candidates) - set(w)
        for m in combinations(rest1 & set(men), 2):
            rest2 = rest1 - set(m)
            for l in permutations(rest2, 2):
                # Ограничение: не две женщины на третьей спец.
                if l[0] in women and l[1] in women:
                    continue
                total_women = sum(1 for group in [w,m,l] for person in group if person in women)
                results.append((w,m,l,total_women))
                if total_women > max_women_total:
                    max_women_total = total_women
                    best_solution = (w,m,l)

    # Вывод результатов
    result_text.delete(1.0, tk.END)
    for idx, (w,m,l,total_women) in enumerate(results, 1):
        result_text.insert(tk.END,
            f"{idx}. Спец1(Ж): {w}, Спец2(М): {m}, Спец3(ЛЮБ): {l} | Женщин всего: {total_women}\n")
    if best_solution:
        optimal_var.set(f"Оптимальное решение: Спец1{best_solution[0]}, Спец2{best_solution[1]}, "
                        f"Спец3{best_solution[2]} | Женщин всего: {max_women_total}")
    else:
        optimal_var.set("Нет допустимых решений.")

# --- GUI ---
root = tk.Tk()
root.title("Распределение вакансий")

frame_input = ttk.Frame(root)
frame_input.pack(padx=10, pady=5)

ttk.Label(frame_input, text="Число женщин:").grid(row=0, column=0)
entry_women = ttk.Entry(frame_input, width=5)
entry_women.insert(0,"3")
entry_women.grid(row=0,column=1)

ttk.Label(frame_input, text="Число мужчин:").grid(row=0,column=2)
entry_men = ttk.Entry(frame_input, width=5)
entry_men.insert(0,"3")
entry_men.grid(row=0,column=3)

btn_calc = ttk.Button(frame_input, text="Рассчитать", command=solve)
btn_calc.grid(row=0,column=4,padx=10)

optimal_var = tk.StringVar()
ttk.Label(root,textvariable=optimal_var,font=("Arial",12,"bold")).pack(pady=(5,0))

result_text = scrolledtext.ScrolledText(root,width=80,height=20,font=("Consolas",10))
result_text.pack(padx=10,pady=(5,10))

root.mainloop()