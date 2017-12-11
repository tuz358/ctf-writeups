#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# shattered-1.pdf: https://shattered.io/static/shattered-1.pdf
# shattered-2.pdf: https://shattered.io/static/shattered-2.pdf

import hashlib


data1 = open('./shattered-1.pdf', 'rb').read()
data2 = open('./shattered-2.pdf', 'rb').read()

filesize = (2017*1024 + 2018*1024) / 2 # = 2065920

data1 += 'A'*(filesize - len(data1))
data2 += 'A'*(filesize - len(data2))

open('collision1.pdf', 'wb').write(data1)
open('collision2.pdf', 'wb').write(data2)

print('SHA1hash:\n-----')
print('collision1.pdf: {0}'.format(hashlib.sha1(data1).hexdigest()))
print('collision2.pdf: {0}'.format(hashlib.sha1(data2).hexdigest()))
print('-----')
