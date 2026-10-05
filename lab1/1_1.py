import matplotlib.pyplot as plt

T = 0.2
K_CO = 1

K_FB_values = [0, 2, 5, 6.5, 8.5, 10]

t_end = 6
k = np.arange(0, int(t_end / T) + 1)
t = k * T

plt.figure(figsize=(10, 6))

for K_FB in K_FB_values:
    z = 1 - K_FB * K_CO * T

    # Значения выхода в моменты дискретизации
    y = 1 - z**k

    # Линия между отсчётами соответствует
    # непрерывному интегратору в Simulink
    plt.plot(t, y, label=rf'$K_{{FB}}={K_FB}$')

plt.xlabel('t, с')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.ylim(-1,3.7)
plt.xlim(0, t_end)

plt.tight_layout()
plt.show()