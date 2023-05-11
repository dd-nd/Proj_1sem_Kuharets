# class TriangleChecker:
#     def __init__(self, b):
#         self.b = b
#
#     def is_triangle(self):
#         pass
#

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