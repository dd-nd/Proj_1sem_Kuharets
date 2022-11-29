# Дан список размера N и целое число K (1 < K < N).
# Осуществлять сдвиг элементов списа влево на K позиций.
# Последние K элементов полученного списка положить равными 0
from random import randint

n = int(input("Количество элементов в списке -> "))
k = int(input("Введите число K (1 < K < N) -> "))
# if 1 < k < len(n):
#     k = int(input("Введите число (1 < K < N) -> "))
lst = []
for i in range(n):  # наполняем список
    a = randint(1, 20)
    lst.append(a)
print(lst)
x = 0
while x < k:
    lst.pop(0)
    lst.append(0)
    x += 1
print(lst)