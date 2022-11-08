# Описать функцию ShiftRight3(A, B, C),
# выполняющую правый циклический сдвиг.
lst = list(map(float, input().split()))
def shiftRight3():
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
print(*shiftRight3())

