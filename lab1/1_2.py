import numpy as np
import matplotlib.pyplot as plt

# Период дискретизации
T = 0.2

# Матрицы дискретной системы
A = np.array([
    [1.0, 0.2],
    [0.0, 1.0]
])

B = np.array([
    [0.02],
    [0.2]
])

C = np.array([
    [1.0, 0.0]
])

# Коэффициенты обратной связи для пяти наборов корней
K_values = [
    np.array([[0.0,   1.0]]),
    np.array([[90.0, 10.0]]),
    np.array([[30.0,  8.0]]),
    np.array([[50.0,  5.0]]),
    np.array([[50.5,  5.95]])
]

# Желаемые собственные числа
roots = [
    (1.0, 0.8),
    (-1.0, -0.8),
    (0.0, -0.2),
    (1j, -1j),
    (-0.1 + 0.9j, -0.1 - 0.9j)
]

# Начальные условия:
# x1(0) = y(0) = 1
# x2(0) = y'(0) = 0
x0 = np.array([
    [1.0],
    [0.0]
])

# Время моделирования
t_end = 10
N = int(t_end / T) + 1

k = np.arange(N)
t = k * T

for i, K in enumerate(K_values):
    plt.figure(figsize=(11, 7))

    # Матрица динамики замкнутой системы
    F = A - B @ K

    # Вектор состояния
    x = x0.copy()

    # Массив для хранения выхода
    y = np.zeros(N)

    for n in range(N):
        y[n] = (C @ x).item()
        x = F @ x

    # Вывод матрицы и фактических собственных чисел
    print(f'Набор {i + 1}')
    print('K =', K)
    print('F =')
    print(F)
    print('Собственные числа:', np.linalg.eigvals(F))
    print()

    # Переходный процесс
    plt.plot(
        t,
        y,
        marker='o',
        markersize=3,
        linewidth=2.,
        label=rf'Набор {i + 1}: $z_1={roots[i][0]},\ z_2={roots[i][1]}$',
        color='#0ABAB5'
    )

    plt.axhline(0, linewidth=0.8)

    plt.xlabel('t, с')
    plt.ylabel('y(k)')
    plt.title('Переходные процессы замкнутых систем')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, t_end)

    plt.tight_layout()
    plt.savefig(f'lab1/img1_2/lab1_2_set_{i + 1}.png', dpi=300)
    plt.close()
    