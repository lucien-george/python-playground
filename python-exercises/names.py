# -*- coding: utf-8 -*-
names = ''
with open('names.txt') as n:
    names += n.read()
names = names.split('\n')
print(names)