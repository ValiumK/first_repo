# 09.09.2021 Упражнение с классами
class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

f_user = User('john', 'smith', 38)
s_user = User('ivan', 'sidoroff', 40)

print(f"User first name is {f_user.first_name.title()}.")
print(f"User last name is {f_user.last_name.title()}.")
print(f"User age is {f_user.age}.")

print(f"User first name is {s_user.first_name.title()}.")
print(f"User last name is {s_user.last_name.title()}.")
print(f"User age is {s_user.age}.")
       


