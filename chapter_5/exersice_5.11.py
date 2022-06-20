numbers = [number for number in range(1, 10)]
for ordinal_number in numbers:
	if ordinal_number == 1:
		print('1st')
	elif ordinal_number == 2:
		print('2nd')
	elif ordinal_number == 3:
		print('3rd')
	else:
		print(f'{ordinal_number}th')
