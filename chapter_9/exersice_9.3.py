class User():

    def __init__(self, first_name, last_name, username, password, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email

    def describe_user(self):
        print(f'Имя пользователя - {self.first_name}\nФамилия пользователя - {self.last_name}\nНикнейм - {self.username}\nПароль - {self.password}\nПочта - {self.email}')

    def great_user(self):
        print(f'\nПриветствую вас - {self.first_name} "{self.username}" {self.last_name}')

user = User('Руслан', 'Асхадуллин', 'RusianO', '12345', 'ashadullinruslan@rambler.ru')

user.describe_user()
user.great_user()