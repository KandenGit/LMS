# Ввод чисел
number = float(input('Введи число от которого будем искать процент: '))
percent = float(input('Число, которое будет представлено в процентах: '))

# Преобразование в процент
percent = number * (percent / 100)
print(f'Это число в процентах: {percent:.2f}')