favorite_fruits = ['бананы', 'манго', 'яблоки']
if 'бананы' in favorite_fruits:
	print(f'Твои любимые фрукты {favorite_fruits[0]}?')
	if input('Ответ \'Да\' или \'Нет\': ') == 'Да':
		print('Круто')
	else:
		print('Не круто')
