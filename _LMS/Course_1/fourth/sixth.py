text = str(input('Введите текст: '))

for i in range(0, text.count('(')):
    open_brack = text.find("(")
    close_brack = text.find(")") + 1

    on_brack = text[open_brack:close_brack]
    #print(on_brack)
    text = text.replace(on_brack, "")
    print(text)