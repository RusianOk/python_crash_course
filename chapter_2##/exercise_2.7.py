'''Удаление пропусков: сохраните имя пользователя в переменной. Добавьте в начале
и в конце имени несколько пропусков. Проследите за тем, чтобы каждая служебная последовательность , "\t" и "\n", встречалась по крайней мере один раз.
Выведите имя, чтобы были видны пропуски в начале и конце строки. Затем выведите его снова с использованием каждой из функций удаления пропусков: lstrip(), rstrip() и strip().'''

name = ' \tRuslan \nAskhadullin '
print(name)
print(name.lstrip(), name.rstrip(), name.strip(), sep='\n')