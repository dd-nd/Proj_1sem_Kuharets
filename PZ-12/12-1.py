# Проверить есть ли в последовательности целых N чисел число K

from random import randint
n = int(input("Введите кол-во чисел в списке -> "))
k = int(input("Введите число -> "))
f = False
lst = [randint(0, 20) for i in range(n)]
print(lst)

for i in lst:
    if i == k:
        f = True
print(f)