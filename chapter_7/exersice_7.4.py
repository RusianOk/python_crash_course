active = True
toppings_pizza = []

while active:
    toping = input("Пожалуйста введите сколько угодно дополнений для пиццы. Как закончите выбор напишите 'quit': ") #Пользователь вводит топинг

    if toping == 'quit': #Если пользователь захочет выйти ему нужно прописать 'quit' и цикл завершится
        break

    toppings_pizza.append(toping) #Cохраняет весь заказ в отдельный список
    print(f"'{toping}', включен в заказ")

