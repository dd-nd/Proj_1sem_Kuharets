# В матрице найти максимальный положительный элемент
from random import randint

r = int(input("Введите кол-во строк -> "))
c = int(input("Введите кол-во столбцов -> "))
a = [[randint(0, 20) for i in range(r)] for i in range(c)]
print(a)
x = 0
for item in a:
    if x <= int(item):
        x = int(item)   #er
print(f'Максимальный эл-т -> {x}')