n = int(input("Введите число: "))

divisors = []
for i in range(1, n+1):
    if n % i == 0:
        divisors.append(i)


print(divisors)