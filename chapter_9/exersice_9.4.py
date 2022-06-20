class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def read_number_served(self):
        print(f'Колличество обслуженных посетителей = {self.number_served}')

    def set_number_served(self, serv):
        self.number_served = serv

    def increment_number_served(self, sum_serv):
        self.number_served += sum_serv

    def describe_restaurant(self):
        print(f'Название ресторана - {self.restaurant_name}. Тип кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'Ресторан открыт')

restaraunt = Restaurant('ПиццаОтНадюши', 'Итальянская')
restaraunt.read_number_served()
restaraunt.increment_number_served(3)
restaraunt.read_number_served()
restaraunt.increment_number_served(3)
restaraunt.read_number_served()
restaraunt.increment_number_served(3)
restaraunt.read_number_served()