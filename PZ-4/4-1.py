# Дано вещественное число A и целое число N(>0). найти A^N
try:
    a = float(input("Введите А"))
    n = int(input("Введите степень N"))
    print(round(a**n, 2))
except:
    print("Error")
