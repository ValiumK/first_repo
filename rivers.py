# 29.08.2021 Упражнение со словарями и циклом for
rivers = {
    'nile': 'egypt', 
    'volga': 'russia', 
    'don': 'russia', 
    'temes': 'britain'
    }

for river, country in rivers.items():
    print(f"{river.title()} runs throught {country.title()}.")

for river in rivers:
    print(river.title())
# Тут добавил вызов множества set(), чтобы исключить дубликаты
for country in set(rivers.values()):
    print(country.title())