print('Список гостей расширился')
invited = ['Lada', 'Maks', 'Mother']
invited.insert(0, 'Kit')
invited.insert(2, 'Marusya')
invited.append('Anna')
print(f'Hello, {invited[0]}\nHello, {invited[1]}\nHello, {invited[2]}\nHello, {invited[3]}\nHello, {invited[4]}\nHello, {invited[5]}')
print('В итоге приглашаются всего два гостя')
print(invited.pop(), 'sorry')
print(invited.pop(), 'sorry')
print(invited.pop(), 'sorry')
print(invited.pop(), 'sorry')
print(f'{invited[0]} - OK\n{invited[1]} - OK')
del invited[0]
del invited[0]
print(f'Приглашения отменяются, список гостей пуст - ', invited)