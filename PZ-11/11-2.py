# Из файла text18-13.txt вывести на экран его содержимое, кол-во сим-ов в тексте.
# Сформировать новый файл, в который поместить текст в стихотворной форме,
# предварительно вставив после строки N (N задает пользователь) произвольную фразу.

f = open('text18-13.txt', encoding='UTF-8')
f1 = open('text18-13.txt', encoding='UTF-8')

data = f.read()
c = len(data)
print(data)
print(f'Кол-во символов в файле: {c}')
try:
    n = int(input('Введите номер строки-> '))
    string = input('Введите строку-> ')
except:
    print('Error')
lst=[]
for line in f1.readlines():
    line2 = line.replace('\n', '')
    lst.append(line2)
lst.insert(n-1, string)
f2 = open('text18-13-new.txt','w', encoding='UTF-8')
for item in lst:
    f2.write('%s\n' % item)

f.close()
f1.close()
f2.close()