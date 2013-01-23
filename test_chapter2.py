#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import fractions
import math

from chapter2 import *

class TestChapter2(unittest.TestCase):
	'''
	Test class for SICP chapter 2 emulate functions.
	'''
	def test_add_rat(self):
		one_half = make_rat(1, 2)
		#print_rat(one_half)
		one_third = make_rat(1, 3)
		#print_rat(one_third)
		res = add_rat(one_half, one_third)
		self.assertEqual(make_rat(5, 6), res)

	def test_mul_rat(self):
		one_half = make_rat(1, 2)
		one_third = make_rat(1, 3)
		res = mul_rat(one_half, one_third)
		self.assertEqual(make_rat(1, 6), res)

	def test_add_rat_simplification(self):
		one_third = make_rat(1, 3)
		res = add_rat(one_third, one_third)
		#self.assertEqual(make_rat(2, 3), res)
		self.assertEqual(numer(res), 2)
		self.assertEqual(denom(res), 3)
	
	def test_car(self):
		cs = cons(1, 2)
		self.assertEqual(1, car(cs))

	def test_car(self):
		cs = cons(1, 2)
		self.assertEqual(2, cdr(cs))

	def test_list2(self):
		res = list2(1, 2, 3, 4)
		self.assertEqual(1, car(res))
		self.assertEqual(2, car(res))
		self.assertEqual(3, car(res))
		self.assertEqual(4, car(res))

	def test_list_ref(self):
		pass

if __name__ == '__main__':
	print(__file__)
	unittest.main()
