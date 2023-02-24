# В строках файла dates1.txt все даты представить 
# в виде подстроки. Поместить в новый файл все 
# даты февраля в формате дд/мм/гггг
# import re

# date_re = r'[0123]?\d[./\\][01]?\d[./\\]20[0123][01]'

# открываем файл
# name: str = input ("Введите имя входящего файла")
# f = open (name, "r")  
with open('dates1.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

# В эту переменную сохранится найденная дата
# date_str = ''

# for line in lines:
  # поиск шаблона в строке
#   re_result = re.search(date_re, line)
  # если нашли
#   if re_result:
    # сохраняем в переменную и завершаем цикл поиска
    # date_str = re_result.group(0)
    # break