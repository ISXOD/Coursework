import math
import matplotlib.pyplot as plt

# Вычислительный эксперимент по исследованию свободного падения тела в полях тяготения разных планет
# Меркурий, Венера, Земля, Марс, Юпитер, Сатурн, Уран, Нептун
G = 6.674e-11
h = 100


def get_g(property):
    return G * property[1] / (property[0])**2


names_planet = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
planets_property = {'Меркурий': [2439.7e3, 3.3e23], 'Венера': [6051.8e3, 4.87e24], 'Земля': [6371e3, 5.97e24],
                    'Марс': [3389e3, 6.42e23], 'Юпитер': [71492e3, 1.9e27], 'Сатурн': [603e5, 5.68e26],
                    'Уран': [25362e3, 8.68e25], 'Нептун': [24622e3, 1.02e26]}


for i in names_planet:
    g = get_g(planets_property[i])
    print(g)
    t0 = math.sqrt(2*h/g)
    print(t0)
    t = 0
    mas_x, mas_S, mas_V = [], [], []
    while t0 - t > 0.01:
        S = h - g * t**2 / 2
        V = g * t
        mas_S.append(S)
        mas_x.append(t)
        mas_V.append(V)
        t += 0.1
    plt.figure()
    plt.title("График S(t) на планете " + i)
    plt.xlabel("t")
    plt.ylabel("S")
    plt.plot([0, t], [0, 0])
    plt.plot(mas_x, mas_S)
    plt.plot([0, 0], [0, h])

    print(i, mas_V[-1])
    plt.figure()
    plt.title("График V(t) на планете " + i)
    plt.xlabel("t")
    plt.ylabel("V")
    plt.plot([0, t], [0, 0])
    plt.plot(mas_x, mas_V)
    plt.plot([0, 0], [0, mas_V[-1]])
plt.show()