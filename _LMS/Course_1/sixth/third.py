# для оценивания: example1

def example1(first: float, second: float, third: float = 0):
    max_num = first if first > second else second
    max_num = max_num if max_num > third else third
    return f'Максимальное из переданных значений: {max_num}'


def example2(first: float, second: float, *args):
    my_list = [first, second, *args]
    set(my_list)

    return my_list[-1]


func = example1(35, 83, 20)
print(func)
