# Дана строка. Подсчитать количество цифр в ней
try:
    a = input("Введите строку -> ")
    count = 0
    for i in a:
        if i.isdigit():
            count += 1
    if count == 0:
        print("Цифр нет")
    else:
        print(count)
except:
    print("Error")