# -*- coding: utf-8 -*-

Glos = {
    'Переменная': ' — это простейшая именованная структура данных, в которой может быть сохранён промежуточный или конечный результат работы программы. Переменную в Python создать очень просто — нужно присвоить некоторому идентификатору значение при помощи оператора присваивания «=».',
    'Строка': ' — базовый тип представляющий из себя неизменяемую последовательность символов; str от «string» — «строка». obj : Объект, который требуется привести к строке, либо получить для него «неформальное» строковое представление. Строки относятся к неизменяемым последовательностям.',
    'Множество': ' — тип данных похожий на словарь, но все значения в нем уникальны'
}
for v, k in Glos.items():
    print(f'\t\n{v}{k}')