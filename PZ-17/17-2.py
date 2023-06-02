# Создайте базовыЙ класс "Человек" со свойствами "имя", "возраст" 
# и "пол". От этого класса унаследуйте классы "мужчина" и 
# "женщина" и добавьте в них свойства, связанные с социальными 
# положениями, например "семейное положение", "количество детей" и т.д.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Person):
    def __init__(self, name, age, gender, marital_status, number_of_children):
        super().__init__(name, age, gender)
        self.marital_status = marital_status
        self.number_of_children = number_of_children

class Woman(Person):
    def __init__(self, name, age, gender, marital_status, number_of_children):
        super().__init__(name, age, gender)
        self.marital_status = marital_status
        self.number_of_children = number_of_children

man1 = Man('Антон', 24, 'М', 'Женат', 2)
woman1 = Woman("Наталья", 32, "Ж", "Одна", 0)

print("Человек №1:", man1.name, man1.age, man1.gender, man1.marital_status, man1.number_of_children)
print("Человек №2:", woman1.name, woman1.age, woman1.gender, woman1.marital_status, woman1.number_of_children)