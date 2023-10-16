series_of_num = input('Введите ряд чисел (через пробел): ')
nums_list = series_of_num.split()
degree = int(input('Степень возведеня всех чисел: '))
new_list = []


for i in range(0, len(nums_list)):
    new_list.append(int(nums_list[i]) ** degree)


print(new_list)