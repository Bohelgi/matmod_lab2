import numpy as np
from scipy.optimize import linprog

l = [-1, -3, 0, 5, 0, 0]

c = [[2, 4, 1, 2, 0, 0], [-3, 5, 0, -3, 1, 0], [4, -2, 0, 8, 0, 1]]

d = [28, 30, 32]

x_bounds = [(0, 6), (0, 6), (0, 6), (0, 6), (0, 6), (0, 6)]

result = linprog(l, A_ub=c, b_ub=d, bounds=x_bounds, method='simplex', options={"disp": True})

if result.success:
    print("Оптимальне рішенння:")
    for i, (var, value) in enumerate(zip(['x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6'], result.x)):
        print(f"{var}: {value:.2f}")
    print(f"Оптимальне значення цільової функції: {result.fun:.2f}")
else:
    print("Оптимізація не була успішною. Перевірте вхідні обмеження.")

print("Статус:", result.message)