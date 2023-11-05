n = int(input('Число: '))

simply_list = []


simply_list.append(3) if n >= 3 else ...
simply_list.append(5) if n >= 5 else ...
for i in range(2, n+1):
    if i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        simply_list.append(i)

print(set(simply_list))