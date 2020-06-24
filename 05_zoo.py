#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1,'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.append('rooster')
zoo.append('ostrich')
zoo.append('lark')
print(zoo)


# уберите слона
#  и выведите список на консоль
zoo.pop(3)
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
#zoo.index('lion')
print('Лев сидит в клетке',zoo.index('lion'))
print('Жаворонок сидит в клетке',zoo.index('lark'))

