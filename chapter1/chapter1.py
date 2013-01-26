#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import fractions

'''
Try for emulating SICP Chapter 1 source.
'''

def square(x):
	'''
	P.6
	'''
	return x*x
	
def sum_of_squares(x, y):
	'''
	P.7
	'''
	return square(x)+square(y)

def abs2(x):
	'''
	P.9
	'''
	return -x if x < 0 else x

def and2(*predicates):
	'''
	P.10
	'''
	for pred in predicates:
		if pred == False: return pred
	return True

def or2(*predicates):
	'''
	P.10
	'''
	for pred in predicates:
		if pred == True: return pred
	return False

def not2(pred):
	'''
	P.10
	'''
	return False if pred == True else True

def gte(x, y):
	'''
	P.11
	'''
	return not2(x < y)

def lte(x, y):
	'''
	Less than equal function.
	'''
	return not2(x > y)

def average(x, y):
	'''
	P.13
	'''
	return (x+y)/2
		
def sqrt_v0(x):
	'''
	P.12
	'''
	def good_enough(guess):
		return abs2(square(guess)-x) < 0.001

	def improve(guess):
		return average(guess, x/guess)
	
	def sqrt_iter(guess):
		if good_enough(guess):
			return guess
		else: 
			return sqrt_iter(improve(guess))

	return sqrt_iter(1.0)	

def fractorial(n):
	'''
	P.19
	'''
	def fact_iter(product, counter, max_count):
		if counter > max_count:
			return product
		else:
			return fact_iter(counter*product, counter+1, max_count)

	return fact_iter(1, 1, n)		
	
	#if n == 1:
	#	return 1
	#else:
	#	return n*fractorial(n-1)
	
def fib(n):
	'''
	P.21
	'''
	def fib_iter(a, b, count):
		if count == 0:
			return b
		else:
			return fib_iter(a+b, a, count-1)
	
	return fib_iter(1, 0, n)
	
def first_denomination(kinds_of_coins):
	'''
	P.23
	'''
	coins = {
		1 : 1,
		2 : 5,
		3 : 10,
		4 : 25,
		5 : 50
	}
		
	return coins[kinds_of_coins]

def cc(amount, kinds_of_coins):
	'''
	P.22
	'''
	if amount == 0:
		return 1
	elif or2(amount<0, kinds_of_coins==0):
		return 0
	else:
		return cc(amount, kinds_of_coins-1) + \
		cc(amount-first_denomination(kinds_of_coins), kinds_of_coins)
			
def count_change(amount):
	'''
	P.22
	'''
	return cc(amount, 5)

def expt_iter(b, counter, product):
	'''
	P.25
	'''
	if counter == 0:
		return product
	else:
		return expt_iter(b, counter-1, b*product)

def expt(b, n):
	'''
	P.25
	'''
	return expt_iter(b, n, 1)

def is_even(n):
	'''
	P.25
	'''
	return n % 2 == 0	
	
def fast_expt(b, n):
	'''
	P.25
	'''
	if n == 0:
		return 1
	elif is_even(n):
		return square(fast_expt(b, n/2))
	else:
		return b*fast_expt(b, n-1)	

def gcd(a, b):
	'''
	P.27
	'''
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

def is_divides(a, b):
	'''
	P.28
	'''
	return b % a == 0

def find_divisor(n, test_divisor):
	'''
	P.28
	'''
	if square(test_divisor) > n: 
		return n
	elif is_divides(test_divisor, n):
		return test_divisor
	else:
		return find_divisor(n, test_divisor+1)

def smallest_divisor(n):
	'''
	P.28
	'''
	return find_divisor(n, 2)

def is_prime(n):
	'''
	P.28
	'''
	if n == 1:
		return False
	else:
		return smallest_divisor(n) == n

def expmod(base, exp):
	'''
	P.28
	'''
	def _expmod(base, exp, m):
		if exp == 0: 
			return 1
		elif is_even(exp):
			return square(_expmod(base, exp/2, m)) % m
		else: 
			return base * _expmod(base, exp-1, m) % m
	
	return _expmod(base, exp, exp)

def fermat_test(n):
	'''
	P.29
	'''
	def try_it(a):
		return expmod(a, n) == a
	
	return try_it(random.randint(1, n-1))

def is_prime_fast(n, times):
	'''
	P.29
	'''
	if n <= 1:
		return False
	
	if times == 0:
		return True
	elif fermat_test(n):
		return is_prime_fast(n, times-1)
	else:
		return False

def sum2(term, a, nextf, b):
	'''
	P.32
	'''
	if a > b:
		return 0
	else:
		return term(a) + sum2(term, nextf(a), nextf, b)

def inc(n):
	'''
	P.32
	'''
	return n+1

def identity(x):
	'''
	P.32
	'''
	return x

def cube(x):
	'''
	P.31
	'''
	return x * x * x

def sum_integers(a, b):
	'''
	P.32
	'''
	return sum2(identity, a, inc, b)

def sum_cubes(a, b):
	'''
	P.32
	'''
	return sum2(cube, a, inc, b)

def pi_sum(a, b):
	'''
	P.33
	'''
	#Not work. If misprint?
	#def pi_term(x):
	#	return 1.0 / (x * (x + 2))
	#def pi_next(x):
	#	return x + 4	
	#return sum2(pi_term, a, pi_next, b)
	
	if b <= 0:
		return 0
	else:
		return fractions.Fraction(1, a*(a+2)) + pi_sum(a+4, b-1)

def integral(f, a, b, dx):
	'''
	P.33
	'''
	return sum2(f, a+dx/2, lambda x: x+dx, b) * dx

def is_close_enough(x, y):
	'''
	P.38
	'''
	return abs(x-y) < 0.001
	
def is_positive(x):
	'''
	Is x is positive value?
	'''
	return 0 < x

def is_negative(x):
	'''
	Is x is negative value?
	'''
	return x < 0
	
def search(f, neg_point, pos_point):
	'''
	P.38
	'''
	midpoint = average(neg_point, pos_point)
	if is_close_enough(neg_point, pos_point):
		return midpoint
	else:
		test_value = f(midpoint)
		if is_positive(test_value):
			return search(f, neg_point, midpoint)
		elif is_negative(test_value):
			return search(f, midpoint, pos_point)
		else:
			return midpoint

def half_interval_method(f, a, b):
	'''
	P.38
	'''
	a_value = f(a)
	b_value = f(b)
	
	if and2(is_negative(a_value), is_positive(b_value)):
		return search(f, a, b)
	elif and2(is_negative(b_value), is_positive(a_value)):
		return search(f, b, a)
	else:
		raise ValueError("Values are not of opposite sign")

def fixed_point(f, first_guess):
	'''
	P.39
	'''
	TOLERANCE = 0.00001
	
	def is_close_enough(v1, v2):
		return abs(v1 - v2) < TOLERANCE
	
	def tryf(guess):
		next_value = f(guess)
		if is_close_enough(guess, next_value):
			return next_value
		else:
			return tryf(next_value)

	return tryf(first_guess)

def sqrt_v1(x):
	'''
	P.38
	'''
	return fixed_point(lambda y: average(y, x/y), 1.0)

def average_damp(f):
	'''
	P.41
	'''
	return lambda x: average(x, f(x))

def sqrt_v2(x):
	'''
	P.41
	'''
	return fixed_point(average_damp(lambda y: average(y, x/y)), 1.0)

def deriv(g):
	'''
	P.42
	'''
	dx = 0.00001
	return lambda x: (g(x+dx) - g(x)) / dx

def newton_transform(g):
	'''
	P.42
	'''
	return lambda x: x - (g(x) / deriv(g)(x))

def newtons_method(g, guess):
	'''
	P.42
	'''
	return fixed_point(newton_transform(g), guess)

def sqrt_v3(x):
	'''
	P.42
	'''
	return newtons_method(lambda y: square(y) - x, 1.0)

def fixed_point_of_transform(g, transform, guess):
	'''
	P.42
	'''
	return fixed_point(transform(g), guess)

def sqrt_v4(x):
	'''
	P.43
	'''
	return fixed_point_of_transform(lambda y: x/y, average_damp, 1.0)

def sqrt(x):
	'''
	P.43
	'''
	return fixed_point_of_transform(lambda y: square(y)-x, newton_transform, 1.0)

if __name__ == '__main__':
	print(__file__+" is loaded.")

