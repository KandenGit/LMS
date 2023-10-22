def register(*, f_name: str, l_name: str, patronymic: str, age: int):
    birth_year = 2023 - age
    string = f'{l_name} {f_name} {patronymic} {birth_year} г.р. зарегистрирован'

    return string

func = register(f_name="Вячеслав", l_name="Горбачев", patronymic="Сергеевич", age=17)
print(func)