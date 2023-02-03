# Для каждой строки матрицы с нечетным номером найти
# среднее арифметическое ее элементов
from random import randint

r = int(input("Введите кол-во строк -> "))
c = int(input("Введите кол-во столбцов -> "))
a = [[randint(0, 20) for i in range(r)] for i in range(c)]
print(a)    # готовая матрица
b = a[::2]
print(b)    # нечетные строки
x = 0
z = 0
for item in b:
    x += len(item)
    z += sum(item)
print(f'Среднее арифметическое эл-ов -> {round((z/x), 2)}')