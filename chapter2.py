#!/usr/bin/python3
# -*- coding: utf-8 -*-

import chapter1 as cp1

'''
Try for emulating SICP Chapter 2 source.
'''

def liner_combination(a, b, x, y):
	'''
	P.45
	'''
	return a * x + b * y

def make_rat(n, d):
	'''
	P.48
	'''
	return (n, d)
	#g = cp1.gcd(n, d)
	#return (n/g, d/g)
	
def numer(x):
	'''
	P.48
	'''
	g = cp1.gcd(x[0], x[1])
	return x[0]/g
	#return x[0]

def denom(x):
	'''
	P.48
	'''
	g = cp1.gcd(x[0], x[1])
	return x[1]/g
	#return x[1]

def add_rat(x, y):
	'''
	P.47
	'''
	return make_rat(numer(x)*denom(y) + numer(y)*denom(x), denom(x)*denom(y))

def sub_rat(x, y):
	'''
	P.47
	'''
	return make_rat(numer(x)*denom(y) - numer(y)*denom(x), denom(x)*denom(y))

def mul_rat(x, y):
	'''
	P.47
	'''
	return make_rat(numer(x)*numer(y), denom(x)*denom(y))

def div_rat(x, y):
	'''
	P.47
	'''
	return make_rat(numer(x)*denom(y), denom(x)*numer(y))

def equal_rat(x, y):
	'''
	P.47
	'''
	return numer(x)*denom(x) == numer(y)*denom(y)

def print_rat(x):
	'''
	P.48
	'''
	print(str(numer(x))+"/"+str(denom(x)))

if __name__ == '__main__':
	print(__file__+" is loaded.")
