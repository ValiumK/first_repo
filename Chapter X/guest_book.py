# 11.09.2021 Упражнение с записью в файл. 
# Запуск из терминала python -m guest_book
filename = 'guest_book.txt'

# Приглашение к закрытию программы по окончанию ввода 
prompt = "Enter 'quit' to the end program.\n"

# Цикл while с полями для ввода имени
active = True
while active:   
    print("\nHello.\nPlease tell me your name:")
    f_name = input("First name: \n")
    l_name = input("Last name: \n")

    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
    
#Запись имени в guest_book.txt
with open(filename, 'a') as file_object:
    file_object.write(f_name.title())
    file_object.write(l_name.title())


