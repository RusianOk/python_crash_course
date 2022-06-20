Kit = {
    'name_owner': 'ruslan',
    'kind': 'cat',
}

Marusya = {
    'name_owner': 'ruslan',
    'kind': 'cat',
}

Kodi = {
    'name_owner': 'ruslan',
    'kind': 'dog',
}

Lightning = {
    'name_owner': 'ruslan',
    'kind': 'cat',
}

my_pets = [Kit, Kodi, Marusya, Lightning]

for pet in my_pets:
    print(f"\nВладелец: {pet['name_owner'].title()}\nВид: {pet['kind'].title()}")