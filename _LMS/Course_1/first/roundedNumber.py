# Ввод чисел
num = float(input('Округляемое число: '))
roundedNum = int(input('Кол-во знаков после запятой: '))

# Округление
num = round(num, roundedNum)
print(num)