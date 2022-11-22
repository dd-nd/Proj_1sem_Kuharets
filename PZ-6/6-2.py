# Дано число R и список размера N. Найти два соседних элемента списка, сумма которых наиболее близка к числу R.
# Вывести эти элементы в порядке возрастания их индексов
from random import randint

n = int(input("Количество элементов в массиве -> "))
lst = [1, 2, 3, 4, 5]
for i in range(n):
    a = randint(1, 150)
    lst.append(a)
print(lst)
c = 1
max_sum = lst[c] + lst[c + 1]
for i in range(3, n):
    if lst[i - 1] + lst[i] > max_sum:
        k = i - 1
print(f'lst[{c + 1}] + lst[{c + 2}] = {max_sum}')


# ------------------------------------------
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = int(input("Введите число -> "))
# x = len(lst)
# i = 0
# while i < x:
#     if sum(lst[i], lst[i+1]) == r:
#         print(lst[i], lst[i+1])
#     i += 1
# ## в процессе