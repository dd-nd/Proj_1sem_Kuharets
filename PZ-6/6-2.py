# Дано число R и список размера N. Найти два соседних элемента списка, сумма которых наиболее близка к числу R.
# Вывести эти элементы в порядке вохрастания их индексов
lst = list(map(float,input("Введите значения списка (чиселки) -> ").split()))
r = float(input("Введите число -> "))
x = len(lst)
i = 0
while i < x:
    if sum(int(lst[i]), int(lst[i+1])) == r:
        print(lst[i], lst[i+1])
    i += 1
print(type(lst))
## в процессе