from functools import reduce
list1 = [1, 2, 5, 7, 11, 5, 153]
func = lambda x, y: x if x > y else y
print(reduce(func, list1))