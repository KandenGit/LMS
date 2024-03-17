import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)

x = 2 * np.random.rand(100, 1)  # Один признак
y = 4 + 3 * np.random.randn(100, 1)  # Целевая переменная

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#print("Размер обучающих данных:", x_train.shape)
#rint("Размер тестовых данных:", x_test.shape)

# ВТорое задание
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
print("Среднеквадратичная ошибка:", mse)

# Третье
import matplotlib.pyplot as plt

plt.scatter(x_train, y_train, color='blue', label='Обучающие данные')
plt.scatter(x_test, y_test, color='red', label='Тестовые данные')

#график линии регрессии
plt.plot(x, model.predict(x), color='green', label='Линия регрессии')

plt.xlabel('Признак')
plt.ylabel('Целевая переменная')
plt.title('График линейной регрессии и исходных данных')
plt.legend()

plt.show()
