favorite_numbers = {
    'Lada': [22, 8, 7],
    'Kit': [43, 2],
    'Mother': [8, 4],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers: ")
    for number in numbers:
        print(f"\t{number}")