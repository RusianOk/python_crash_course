favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

workers = ['jen', 'sarah', 'edward', 'ruslan', 'phil', 'lada', 'kit']

for name in workers:
    if name in favorite_language.keys():
        print(f"{name.title()}, спасибо, что уже прошел опрос. {favorite_language[name].title()}, очень крутой язык")
    else:
        print(f"{name.title()}, пройди опрос в ближайшее время! Спасибо!)")
