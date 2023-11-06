n = int(input("Введите число: "))

delitel = []
for i in range(1, n+1):
    if n % i == 0:
        delitel.append(i)


print(delitel)