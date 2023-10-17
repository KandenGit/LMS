s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")


s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")


if len(s1) != len(s2):
    print("Строки не являются анаграммами")
else:
    set1 = set(s1)
    set2 = set(s2)

if set1 == set2:
    print("Строки являются анаграммами")
else:
    print("Строки не являются анаграммами")