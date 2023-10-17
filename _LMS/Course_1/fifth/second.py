string = "младшая сестра фёдора - соня пишет сочинение. она отправляет файлы учительнице."
chars = list(string)
punctuation = ['!', '?', '.']

# первый символ в загавие
chars[0] = chars[0].upper()

for i in range(1, len(chars)):
    if chars[i] in punctuation:
        j = i + 1
        while j < len(chars) and chars[j] == ' ':
            j += 1
        if j < len(chars):
            chars[j] = chars[j].upper()

print(''.join(chars))