list1 = [5, 10, 15, 20, 10]
list2 = [3, 2, 10, 14, 3, 7, 2]

while len(list1) != len(list2):
    list2.append(0) if len(list1) > len(list2) else list1.append(0)


func = lambda l1, l2: l1 + l2

res = map(func, list1, list2)
print(list(res))