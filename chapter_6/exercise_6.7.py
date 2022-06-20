Ruslan = {
    'first_name': 'Ruslan',
    'last_name': 'Askhadullin',
    'age': 22,
    'city': 'Kaliningrad',
}

Lada = {
    'first_name': 'Lada',
    'last_name': 'Kizur',
    'age': 24,
    'city': 'Kaliningrad',
}

Kit = {
    'first_name': 'Lit',
    'last_name': 'Kitay',
    'age': 2,
    'city': 'Kaliningrad',
}

Family = [Ruslan, Lada, Kit]

for info in Family:
    print(f"\nИмя: {info['first_name']}\nФамилия: {info['last_name']}\nВозврат: {info['age']}\nГород проживания: {info['city']}")