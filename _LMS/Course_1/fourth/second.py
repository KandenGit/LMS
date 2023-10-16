string = str(input('Введите строку (не менее 15 символов): '))
new_string = []

def isEven(string: str):
    for i in range(0, len(string)):
        if (i % 2 == 0):
            new_string.append(string[i])
        else:
            continue

    return ''.join(new_string)

print(isEven(string))
