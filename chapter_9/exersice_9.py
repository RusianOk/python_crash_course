class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана - {self.restaurant_name}. Тип кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'Ресторан открыт')

my_res = Restaurant('Пивасик', 'Пиво')

my_res.describe_restaurant()