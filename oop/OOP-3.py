# Инкапсуляция
# _ - доступен в классе и дочерних
# __ - доступен только в классе
# class Point:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
    
#     def set_coord(self, x, y):
#         self._x = x
#         self._y = y
# p = Point()
# p._x = 20
# print(p._x)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
    
#     def set_coord(self, x, y):
#         if type(x) in (int, float) and type(y) in (int, float):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError('Координаты должны быть числами')
        
#     def get_coord(self):
#         return self.__x, self.__y
# p = Point()
# p.set_coord(100, 20)
# # print(p.__x, p.__y)
# print(p.get_coord())

# Задача 1
class Person:
    def __init__(self, name=None):
        self.__name = name

    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

p = Person()
p.set_name('Ilya')
print(p.get_name())