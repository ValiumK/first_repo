# 27.08.2021 Упражнение с числовыми списками
digits = [value for value in range(1,1000001)]
print(min(digits))
print(max(digits))
print(sum(digits))

# Вывод нечетных чисел в цикле for
not_even_numbers = list(value for value in range(1,21,2))
print(not_even_numbers)

# Вывод чисел кратным 3 в цикле for 
digs = list(value*3 for value in range(1,11))
print(digs)

# Вывод чисел в кубе в цикле for
cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(cubes)

# Вывод чисел в кубе в генераторе чисел
cubes = [value**3 for value in range(1,11)]
print(cubes)