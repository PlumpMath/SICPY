#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Try for emulating SICP Chapter 1 source.
'''

def square(x):
	return x*x
	
def sum_of_squares(x, y):
	return square(x)+square(y)

def abs2(x):
	return -x if x < 0 else x

def and2(*predicates):
	for pred in predicates:
		if pred == False: return pred
	return True

def or2(*predicates):
	for pred in predicates:
		if pred == True: return pred
	return False

def not2(pred):
	return False if pred == True else True

def gte(x, y):
	return not2(x < y)

def lte(x, y):
	return not2(x > y)

def sqrt(x):
	def good_enough(guess):
		return abs2(square(guess)-x) < 0.001

	def average(x, y):
		return (x+y)/2

	def improve(guess):
		return average(guess, x/guess)
	
	def sqrt_iter(guess):
		if good_enough(guess):
			return guess
		else: 
			return sqrt_iter(improve(guess))

	return sqrt_iter(1.0)	

def fractorial(n):
	def fact_iter(product, counter, max_count):
		if counter > max_count:
			return product
		else:
			return fact_iter(counter*product, counter+1, max_count)

	return fact_iter(1, 1, n)		
	
	'''
	if n == 1:
		return 1
	else:
		return n*fractorial(n-1)
	'''
	
def fib(n):
	def fib_iter(a, b, count):
		if count == 0:
			return b
		else:
			return fib_iter(a+b, a, count-1)
	
	return fib_iter(1, 0, n)
	
def first_denomination(kinds_of_coins):
	coins = {
		1 : 1,
		2 : 5,
		3 : 10,
		4 : 25,
		5 : 50
	}
		
	return coins[kinds_of_coins]

def cc(amount, kinds_of_coins):
	if amount == 0:
		return 1
	elif or2(amount<0, kinds_of_coins==0):
		return 0
	else:
		return cc(amount, kinds_of_coins-1) + \
		cc(amount-first_denomination(kinds_of_coins), kinds_of_coins)
			
def count_change(amount):
	return cc(amount, 5)

def expt_iter(b, counter, product):
	if counter == 0:
		return product
	else:
		return expt_iter(b, counter-1, b*product)

def expt(b, n):
	return expt_iter(b, n, 1)

def even(n):
	return n/2 == 0	
	
def fast_expt(b, n):
	if n == 0:
		return 1
	elif even(n):
		return square(fast_expt(b, n/2))
	else:
		return b*fast_expt(b, n-1)	

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

def is_divides(a, b):
	return b % a == 0

def find_divisor(n, test_divisor):
	if square(test_divisor) > n: 
		return n
	elif is_divides(test_divisor, n):
		return test_divisor
	else:
		return find_divisor(n, test_divisor+1)

def smallest_divisor(n):
	return find_divisor(n, 2)

def is_prime(n):
	if n == 1:
		return False
	else:
		return smallest_divisor(n) == n

if __name__ == '__main__':
	print(__file__+" is loaded.")

