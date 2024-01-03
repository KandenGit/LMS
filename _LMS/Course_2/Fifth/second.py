import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0, 1, 3000)
y = np.random.normal(3, 4, 3000)

plt.scatter(x, y, marker='<', alpha=0.3, c="green")
plt.title('График ко второму заданию')
plt.xlabel('X')
plt.ylabel('Y', rotation=0)
plt.grid(True)
plt.show()