# Описать функцию ShiftRight3(A, B, C),
# выполняющую правый циклический сдвиг.
a, b, c = map(int, input().split())
def shiftRight3(a, b, c):
    lst = [a, b, c]
    i = 0
    try:
        while i < 3:
            a = lst.pop(-1)
            lst.insert(i, a)
            i += 1
        a = lst.pop(1)
        lst.insert(2, a)
    except:
        print("Error")
    return lst
print(*shiftRight3(a, b, c))

