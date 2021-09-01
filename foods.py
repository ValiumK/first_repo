# 27.08.2021 Упражнение с срезами(slices)
my_foods =['borsch', 'dumplings', 'pizza', 'bacon', 'pies']
friend_foods = my_foods[:]

# Добавляем разные элементы в оба списка
my_foods.append('pasta')
friend_foods.append(' ice cream')

# Вывод списка в цикле for
for my_food in my_foods:
	print(f"My favorite foods are {my_food.title()}")
for friend_food in friend_foods:
	print(f"My friend favorite foods are {friend_food.title()}")

print("My favorite foods are:")
print(my_foods)
print("\nMy friend favorite foods are:")
print(friend_foods)

print("The first three items in the list are:\n")
print(my_foods[:3])
print("The last three items in the list are:\n")
print(my_foods[2:])
print("The middle two items in the list are:\n")
print(my_foods[1:3:1])
