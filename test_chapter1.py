#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

from chapter1 import *;

class TestChapter1(unittest.TestCase):
	'''
	Test class for SICP chapter1 emulate functions.
	'''
	def test_square(self):
		res = square(21)
		self.assertEqual(441, res)

	def test_sum_of_squares(self):
		res = sum_of_squares(3, 4)
		self.assertEqual(25, res)
	
	def test_abs2(self):
		self.assertEqual(5, abs2(5))
		self.assertEqual(0, abs2(0))
		self.assertEqual(5, abs2(-5))
	
	def test_and2(self):
		self.assertEqual(True, and2(7>5, 1<10))
		self.assertEqual(False, and2(7>5, 1>10))

	def test_or2(self):
		self.assertEqual(True, or2(7>5, 1<10))
		self.assertEqual(True, or2(7>5, 1>10))
		
	def test_not2(self):
		self.assertEqual(True, not2(1>10))
		self.assertEqual(False, not2(1<10))
	
	def test_gte(self):
		self.assertEqual(False, gte(1, 2))
		self.assertEqual(True, gte(2, 1))
		self.assertEqual(True, gte(1, 1))

	def test_gte(self):
		self.assertEqual(True, lte(1, 2))
		self.assertEqual(False, lte(2, 1))
		self.assertEqual(True, lte(1, 1))

	def test_sqrt(self):
		self.assertEqual(3.00009155413138, sqrt(9))
		
if __name__ == '__main__':
	print(__file__)
	unittest.main()
		
