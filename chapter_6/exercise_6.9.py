favorite_places = {
    'ruslan': ['new york', 'chicago'],
    'lada': ['dubai']
}

for name, cities in favorite_places.items():
    print(f"{name.title()} хотел(а) бы побывать в:")
    for city in cities:
        print(f"\t{city.title()}")



