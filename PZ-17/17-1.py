# создайте класс "Компьютер" с атрибутами "марка", 
# "процессор" и "оперативная память". напишите метод, 
# который выводит информацию о компьютере в форме 
# "Марка:марка, Процессор:процессор, Оперативная память:память"

class Computer:
    def __init__(self, brand, processor, memory):
        self.brand = brand
        self.processor = processor
        self.memory = memory

    def get_info(self):
        return f'Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.memory}'

computer = Computer('Dell', 'Intel Core i7', '16 ГБ')
info = computer.get_info()
print(info)