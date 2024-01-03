import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(16, 2, 1000)
fig, ax = plt.subplots()
plt.hist(data, color="red", edgecolor="white", alpha=0.5)
plt.show()

# Вывод: на гистограмме видно кол-во пробежавших 100-метровку (ось x)
# (я не совсем понял из чего формируется ось y, поэтому я взял эти значения за оценки (умноженные на 50))