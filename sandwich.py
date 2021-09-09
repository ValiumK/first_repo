# Упражнение с циклом while и списками
sandwich_orders = ['pastrami', 'becon', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {finished_sandwiches} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Упражнение с фунцией def
def favorite_book(book):
    print(f"One my favorite book {book.title()}.")

favorite_book('tikhiy Don')

# Упражнение с фунцией def и использованием произвоного набора аргументов
def make_car(model, hull, **car_info):
    car_info['model_car'] = model
    car_info['hull_type'] = hull
    return car_info

car = make_car('subaru', 'universal', color='black', tow_packge=True)
print(car)



