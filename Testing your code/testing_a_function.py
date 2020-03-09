from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	else:
		continue
	last = input("\nPlease give me a last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\tNeatly formatted name: {formatted_name}.")

#Above works but what if we want to modify so it can handle a middle name, and also not
#break function for names with only first and last - solution: automate testing

#Unit test and Test cases
#The module unittest in Python standard library provides tools for testing your code
#A unit test verifies that one specific aspect of a function's behavior is correct
#A test case is a collection of unit tests that together proves a function works correctly within the full range of situations you want to handle

#A Passing Test
#import unittest module and the function you want to test. Then create a class that inherits from unittest.TestCase
#and write a series of methods to test diff aspects of the functions behavior

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for name_function.py"""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin') #assert methods verify that a result you recieve matches what is expected
		
if __name__ == '__main__':
	unittest.main()

----------------------------------------------------------------
# A Failing Test
def get_formatted_name(first, middle, last):
	full_name = f"{first} {middle} {last}"
	return full_name.title()

# Will return a TypeError for test on Janis Joplin: missing 1 positional argument

--------------------------------------------------------------
# Responding to a failed test - don't change the test, fix the code that caused the error (duh)
def get_formatted_name(first, last, middle=''):
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = "f{first} {last}"
	return full_name.title()
	
--------------------------------------------------------------
# Adding new Tests
class NamesTestCase(unittest.TestCase):
	"""Tests for name_function.py"""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin') #assert methods verify that a result you recieve matches what is expected
	
	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
		
if __name__ == '__main__':
	unittest.main()		



