# 10.09.2021 Упражнение с чтением из файлов
filename = 'learning_python.txt'

"""Чтение всего файла"""
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print (contents)

"""Перебор по строкам"""
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

"""Выводит данные, как строку"""
with open(filename) as file_object:
    lines = file_object.readlines()

tx_string = ''
for line in lines:
    tx_string += line.rstrip()
    
#Заменяем методом replace python на java
print(tx_string.replace('Python', 'Java'))
print(len(tx_string))


