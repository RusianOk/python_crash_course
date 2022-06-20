current_users = ['RuslaN', 'Lada', 'Kit', 'Dima', 'Tr']
new_users = ['Ruslan', '#2', 'anonimus']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print('Нужно новое имя')
	else:
		print(f'Все ок теперь ты - {new_user}')
