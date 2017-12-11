#!/usr/bin/python
#-*- coding: utf-8 -*-

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}'
plain = 'SECCON{' + '*'*26 + '}'
c = 'POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9'
key = ['*']*34

for i in range(len(plain)):
	if plain[i] == '*': continue
	for j in range(len(s)):
		if plain[i] == s[(s.find(c[i]) - s.find(s[j])) % len(s)]:
			key[i] = s[j]

key = ''.join(key)

print('plain:\r\t{0}'.format(plain))
print('key:\r\t{0}'.format(key))
print('crypt:\r\t{0}'.format(c))

