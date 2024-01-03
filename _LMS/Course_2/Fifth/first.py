import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x) ** 3 - np.cos(x)

x_axis = np.linspace(-10, 11, 30)
y_axis = func(x_axis)


plt.plot(x_axis, y_axis, 'g--', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y', rotation=0)
plt.grid(True, alpha=0.5)
plt.text(-3, -1, 'Вот такая моя функция')
plt.show()