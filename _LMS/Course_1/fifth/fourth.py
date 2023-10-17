algebra = input().split()
geometry = input().split()
trigonometry = input().split()


solved_all = set(algebra) & set(geometry) & set(trigonometry)

if solved_all:
    print(" ".join(sorted(solved_all)))
else:
    print("Все три задачи никто не решил")