# Составить список, в который будут включены только согласные буквы и привести их к
# верхнему регистру.

lst = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

lst_1 = [x for i in lst for x in i]
lst_2 = [i for i in lst_1 if i in 'бвгджзклмнпрстфхцчшщБВГДЖЗКЛНМПРСТФХЦЧШЩ']
print([i.upper() for i in lst_2])