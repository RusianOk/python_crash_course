class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана - {self.restaurant_name}. Тип кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'Ресторан открыт')


class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Шоколадное', 'Клубничное', 'Мятное']

    def print_flavors(self):
        print(f'{self.flavors}')

ice_cream_stand = IceCreamStand('МорозокРожок', 'Мороженное')

ice_cream_stand.print_flavors()