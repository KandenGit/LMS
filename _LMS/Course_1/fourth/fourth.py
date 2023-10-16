string = "this is a string with symbol$"

# detect symbol
for i in range(0, len(string)):
    if string[i].isalnum():
        continue
    else:
        symbol = string[i]
        new_string = string.replace(symbol, symbol*2)

print(new_string)