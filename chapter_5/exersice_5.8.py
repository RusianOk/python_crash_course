names = ['admin', 'ruslan', 'lada']
for name in names:
	if name == 'admin':
		print(f'Шо там по репортам, {name}?')
	else:
		print(f'Ты не админ, {name.title()}!')
