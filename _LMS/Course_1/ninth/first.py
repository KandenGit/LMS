# Алгоритм Евклида
num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))

c_num1 = num1
c_num2 = num2

# НОД
while c_num2 > 0:
    c_num1, c_num2 = c_num2, c_num1 % c_num2
    nod = c_num1

# НОК
res = (num1 * num2) / nod
print(res)