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

if __name__ == '__main__':
	print(__file__+" is loaded.")

