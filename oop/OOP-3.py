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

# Задача 2
# Создайте класс Car с приватным атрибутом fuel. Реализуйте методы get_fuel и set_fuel,
# которые позволяют получать и изменять значение этого атрибута соответственно. 
# При изменении значения fuel проверяйте, что оно не станет меньше нуля.
class Car:
    def __init__(self):
        self.__fuel = 0

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, value):
        if value >= 0:
            self.__fuel = value
        else:
            print("Значение топлива не может быть меньше нуля.")

car = Car()
fuel = car.get_fuel()
print("Текущий уровень топлива:", fuel)

car.set_fuel(50)
fuel = car.get_fuel()
print("Новый уровень топлива:", fuel)

car.set_fuel(-10)
fuel = car.get_fuel()
print("Уровень топлива после попытки установки отрицательного значения:", fuel)

# Задача 3
# Создайте класс BankAccount с приватными атрибутами balance и account_number. 
# Реализуйте методы get_balance, deposit и withdraw, которые позволяют получать 
# текущий баланс, пополнять счет и снимать деньги соответственно. При снятии денег 
# проверяйте, что на счету достаточно средств для выполнения операции.
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Счет пополнен на {amount} единиц.")
        else:
            print("Некорректная сумма для пополнения.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Со счета списано {amount} единиц.")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Некорректная сумма для снятия.")

account = BankAccount("1234567890")
balance = account.get_balance()
print("Текущий баланс:", balance)

account.deposit(100)
balance = account.get_balance()
print("Новый баланс после пополнения:", balance)

account.withdraw(50)
balance = account.get_balance()
print("Новый баланс после снятия:", balance)

account.withdraw(200)
balance = account.get_balance()
print("Баланс после неуспешной попытки снятия:", balance)

account.deposit(-20)
balance = account.get_balance()
print("Баланс после неуспешной попытки пополнения:", balance)