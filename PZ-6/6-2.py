# Дано число R и список размера N. Найти два соседних элемента списка, сумма которых наиболее близка к числу R.
# Вывести эти элементы в порядке возрастания их индексов
from random import randint

n = int(input("Количество элементов в списке -> "))
r = int(input("Введите число ->"))
lst = []
c = []
for i in range(n): # напллняем список
    a = randint(1, 20)
    lst.append(a)
print(lst)
for i, x in enumerate(lst):
    c.append(sum(lst[i:i+2]))
c.pop(-1)
print(c)
def near_value(a, r): # ближайшее число к сумме соседних чисел
    found = c[0]
    for i in c:
        if abs(i - r) < abs(found - r):
            found = i
    return found
print(near_value(a, r))