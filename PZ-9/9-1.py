lst = []
d = dict(
    Слон = "Elephant",
    Красный = "Red",
    Сын = "Son",
    Мышь = "Mouse",
    Браузер = "Browser",
    Прыгать = "Jump",
    Почта = "Mail",
    День = "Day",
    Ленивый = "Lazy",
    Ночь = "Night",
)
for i in d:
  lst.append(i)
print(f'Доступные для перевода слова -> {lst}')
a = input("Введите слово -> ")
print(f'Перевод слова -> {d.get(a)}')
