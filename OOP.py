class Vector:
    MIN_CORD = 0
    MAX_CORD = 100

    @staticmethod
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = self.y = y
        print(self.norm2(self.x, self.y))

    def get_corgs(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y

# Задача 1
class Person:
    first_name = str()
    last_name = str()
    kvalik = int()
    def __init__(self, first_name, last_name, kvalik = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.kvalik = kvalik
    
    def prints(self):
        return f'ФИО: {self.last_name} {self.first_name}. Квалификация: {self.kvalik}'
    
    def __del__(self):
        del self.first_name, self.kvalik, self.last_name
        return f'До свидания, мистер {self.last_name} {self.first_name}.'
    
if __name__ == '__main__':
    person1 = Person('Илья', 'Кулиб', 5)
    person2 = Person('Анна', 'Владина', 3)
    person3 = Person('Владимир', 'Кастин', 0)
    print(person1.prints())
    print(person2.prints())
    print(person3.prints())
    del(person3)

# Задача 2
class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

triangle1 = TriangleChecker([4, 1, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([33, 7, 9])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([21, -3, 4])
print(triangle4.is_triangle())

# Задача 3
class Nikola:   # DONE
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def true_name(self):
        if self.name != 'Николай':
            return f'Я не {self.name}, а Николай'
        else:
            return f'Я Николай'


Nikola = Nikola(age=int(input()), name=str(input()))
print(Nikola.true_name())

# Задача 4
import random

class MyList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        return item in self.items

    def sort(self):
        self.items.sort()

my_list = MyList()
for _ in range(15):
    random_num = random.randint(1, 100)
    my_list.add(random_num)
print("Исходный список:", my_list.items)
if my_list.search(2):
    my_list.remove(2)
my_list.sort()
print("Список после удаления и сортировки:", my_list.items)

# Задача 5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(5, 8)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)
