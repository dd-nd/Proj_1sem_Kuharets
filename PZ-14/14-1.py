# В строках файла dates1.txt все даты представить 
# в виде подстроки. Поместить в новый файл все 
# даты февраля в формате дд/мм/гггг
import re

with open('dates1.txt', 'r') as f:
  lines = f.readlines()

str_ = str(lines).replace('\\n', '').replace('\n', '').replace(',', '').replace(';', '').replace("'",'').split(' ')

date_re = r'[012][0-9]\.02\.2022'
date_str = ''
date_arr = []
for date in str_:
  re_result = re.search(date_re, date)
  if re_result:
    date_str = re_result.group(0)
    date_arr.append(date_str.replace('.','/'))
    date_arr.append('\n')
    with open('f_date.txt', 'w') as f:
      f.writelines(date_arr)