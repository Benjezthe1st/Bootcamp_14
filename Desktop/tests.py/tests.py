import unittest

from prime_nos import test_primenos



class Prime_numbers_TestCase(unittest.TestCase):
	
	"""Tests for prime numbers generator function"""
	def test_case_integers(self):
		self.assertEqual(prime_nos.primenumbers(""), 'Please ensure that you pass an integer')

	def test_case_primeNumbers(self):
		self.assertEqual(prime_nos.primenumbers(100), [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]])


	def test_case_Errors(self):
		self.assertEqual(prime_nos.primenumbers(0) )

	def test_case_primeNumbers(self):
		self.assertEqual(prime_nos.primenumbers(10), [2, 3, 5, 7])
		
	def test_case_primeNumbers(self):
		self.assertEqual(prime_nos.primenumbers(2), [1])

	def test_case_primeList_Return(self):
		self.assertIsInstance(prime_nos.primenumbers(7), list)

	
	def test_case_primeNumbers(self):
		self.assertEqual(prime_nos.primenumbers(2), [2, 3, 5, 7, 11, 13, 17, 19])


	def test_case_string(self):
		self.assertEqual(prime_nos.primenumbers('2'), 'Please ensure that you pass an integer')

	def test_case_Negatives(self):
		self.assertEqual(prime_nos.primenumbers(-6), [])


	def test_case_list(self):
		self.assertEqual(prime_nos.primenumbers([3, 4, 60]), 'Please ensure that you pass an integer')
		

	


if __name__ == '__main__':
	unittest.main()
