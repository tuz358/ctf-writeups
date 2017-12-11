#!/usr/bin/python
#-*- coding: utf-8 -*-

s   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}'
c   = 'POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9'
key = ('_KP2Za__aZ2PK_'*3)[:34]

plain = ['*']*len(c)

for i in range(len(c)):
	plain[i] = s[(s.find(c[i]) - s.find(key[i]) ) % len(s)]

print(c)
print(key)
print(''.join(plain))
