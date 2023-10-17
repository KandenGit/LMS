num_of_str = int(input('Сколько городов: '))
city_list = []

# заполнение списка
for i in range(0, num_of_str):
    city_name = str(input('Название города: '))
    city_list.append(city_name)


print(len(set(city_list)))