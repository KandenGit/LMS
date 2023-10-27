list1 = [19, 13, 38, 7, 12]

func = lambda x: x % 13 == 0 or x % 19 == 0
res = filter(func, list1)
print(list(res))