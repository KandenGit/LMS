import numpy as np

# задача 1
arr = np.random.randint(1, 11, size=100)
biggest_7 = np.count_nonzero(arr > 7)
percent = biggest_7 / len(arr) * 100

#print(f"Процент элементов болше 7: {percent}")

# Задача 2
arr = np.random.randint(1, 11, size=1000)
biggest_7 = np.count_nonzero(arr > 7)
percent = biggest_7 / len(arr) * 100
p = biggest_7 * 0.2
print(f"{p:.1f}")

# Задача 3
matr = np.tile(np.arange(1, 11), (10, 1))
print(matr)

# Задача 4
matr_sum = np.sum(matr, axis=0)
print(matr_sum)
