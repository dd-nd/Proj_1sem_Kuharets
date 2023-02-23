# В матрице найти максимальный положительный элемент, кратный 4
from random import randint

r = int(input("Введите кол-во строк -> "))
c = int(input("Введите кол-во столбцов -> "))
a = [[randint(-20, 23) for i in range(r)] for i in range(c)]
print(a)
x = 0
for i in a:
    for item in i:
        if x <= item and item % 4 == 0 and item > 06:
            x = item
print(f'Максимальный эл-т -> {x}')