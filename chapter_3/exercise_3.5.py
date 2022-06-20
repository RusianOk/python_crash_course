invited = ['Lada', 'Maks', 'Mother']
print(invited.pop(1))

#Изменил список и заменил гостя
invited.insert(1, 'Kit')

print(f'Hello, {invited[0]}\nHello, {invited[1]}\nHello, {invited[2]}')