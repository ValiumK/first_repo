# 28.08.2021 Упражнение if-else со списками 
users =['admin', 'john', 'maria', 'anna', 'vasya']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging again!")

# Упражнение со множественными списками
current_users = ['admin', 'john', 'maria', 'anna', 'vasya']
new_users = ['admin', 'maria', 'walter', 'bill', 'aleksander']

for new_user in new_users:
    if new_user in current_users:
        print(f"Username unaviable.")
    else:
        print(f"{new_user} is aviable")
 