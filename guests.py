# 25.08.2021 Упражнение со списками
guests = ['alexander', 'vitaly', 'dmitry']
# Ниже меняется имя гостя, который не придет
guests[2] = 'yury'

#Удаляем гостей и извиняемся
remove_guests = guests.pop()
print(f"Dear {remove_guests.title()}, I'm sorry, but I have to cancel the invitation")
remove_guests = guests.pop(1)
print(f"Dear {remove_guests.title()}, I'm sorry, but I have to cancel the invitation")

addguests = []
addguests.insert(0,'vasiliy')
addguests.insert(1,'georgiy')
addguests.append('christodul')

# Удаляем гостей и извиняемся
remove_guests = addguests.pop()
print(f"Dear {remove_guests.title()}, I'm sorry, but I have to cancel the invitation")
remove_guests = addguests.pop(1)
print(f"Dear {remove_guests.title()}, I'm sorry, but I have to cancel the invitation")

# Подтверждаем приглашения
print(f"Dear {guests[0].title()}, your invitation is valid.")
print(f"Dear {addguests[0].title()}, your invitation is valid.")

# Просто смотрим, как работает комманда delete
del guests[0]
del addguests[0]
print(guests)
print(addguests)