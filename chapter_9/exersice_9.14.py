from secrets import choice


lottery = [1, 2, 'e', 3, 4, 5, 6, 'w', 't', 7, 8, 9, 'q', 'z', 10]
win = []

for i in range(4):
    win.append(choice(lottery))

print(f'Комбинация для выигрыша - {win}')