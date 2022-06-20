def make_shirt(Текст, Размер = 'xs'):
    print(f"Размер {Размер}, Текст '{Текст}'")

def make_shirt2(Текст, Размер):
    print(f"Размер {Размер}, Текст '{Текст}'")

def make_shirt3(Текст = 'Durachek?', Размер = 'xs'):
    print(f"Размер {Размер}, Текст '{Текст}'")

make_shirt('Hello')
make_shirt2('Hello', 21)
make_shirt3()