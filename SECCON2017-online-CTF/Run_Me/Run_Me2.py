#!/usr/bin/python
#-*- coding: utf-8-

def f(n):
	a,b = 0,1
	for i in range(1, n):
		a,b = b, a+b
	return b

print 'SECCON{' + str(f(11011))[:32] + '}'
