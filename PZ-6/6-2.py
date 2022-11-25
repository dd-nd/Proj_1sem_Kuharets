# Дано число R и список размера N. Найти два соседних элемента списка, сумма которых наиболее близка к числу R.
# Вывести эти элементы в порядке возрастания их индексов
from random import randint

n = int(input("Количество элементов в списке -> "))
r = int(input("Введите число ->"))
lst = []
c = []
dop = []
for i in range(n): # наполняем список
    a = randint(1, 20)
    lst.append(a)
print(lst)
for i, x in enumerate(lst):
    dop.append(lst[i:i+2])
    c.append(sum(lst[i:i+2]))
c.pop(-1)
print(f'Суммы соседних чисел -> {c}')
def near_v(a, r): # ближайшее число к сумме соседних чисел
    found = c[0]
    for i in c:
        if abs(i - r) < abs(found - r):
            found = i
            for j in range(len(c)):
                if c[j] == found:
                    print(f'Соседние числа -> {dop[j]}')
    return found
print(f'Ближайшая сумма -> {near_v(a, r)}')