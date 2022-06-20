names = []
if names:
	for name in names:
		if name == 'admin':
			print(f'Шо там по репортам, {name}?')
		else:
			print(f'Ты не админ, {name.title()}!')
else:
	print('Почему список пуст?')
