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

# Задача
class Person:
    def __init__(self, first_name, last_name, kvalik = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.kvalik = kvalik
    
    def __str__(self):
        return f'ФИО: {self.last_name} {self.first_name}. Квалификация: {self.kvalik}'
    
    def __del__(self):
        del self.first_name, self.kvalik, self.last_name
        return f'До свидания, мистер {self.last_name} {self.first_name}.'
    

person1 = Person('Илья', 'Кулиб', 5)
person2 = Person('Анна', 'Владина', 3)
person3 = Person('Владимир', 'Кастин', 0)

del person3