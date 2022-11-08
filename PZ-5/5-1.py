# Найти сумму чисел ряда 1,2,3…60 с использованием
# функции нахождения суммы. Использовать локальные переменные.
def summa():
    i = 1
    s = 0
    try:
        while i <= 60:
            s = i + s
            i += 1
    except:
        print("Error")
    return s
print(summa())