'''Изменение списка гостей: вы только что узнали, что один из гостей прийти не сможет,
поэтому вам придется разослать новые приглашения. Отсутствующего гостя нужно заменить кем-то другим.
• Начните с программы из упражнения 3.4. Добавьте в конец программы команду
print для вывода имени гостя, который прийти не сможет.
• Измените список и замените имя гостя, который прийти не сможет, именем нового
приглашенного.
• Выведите новый набор сообщений с приглашениями — по одному для каждого
участника, входящего в список.'''

invited = ['Lada', 'Maks', 'Mother']
print(invited.pop(1))

#Изменил список и заменил гостя
invited.insert(1, 'Kit')

print(f'Hello, {invited[0]}\nHello, {invited[1]}\nHello, {invited[2]}')