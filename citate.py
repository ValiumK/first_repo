# 24.08.2021 Упражнение по фоматированию стоки 
first_name = " albert  "
last_name = " einstein  "
first_name = first_name.strip()
last_name = last_name.strip()
famous_person = f"{first_name} {last_name}"
message = f'{famous_person.title()} once said:\n\t"A person who never made mistake, never tried another new."'
print(message)