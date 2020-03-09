# Six commonly used assert methods from the unittest.TestCase class:
#assertEqual(a, b)			Verify a==b
#assertNotEqual(a, b)		Verify a != b
#assertTrue(x)				Verify x is True
#assertFalse(x)				Verify x is False
#assertIn(item, list)		Verify that item is in list
#assertNotIn(item, list)	Verify that item is not in list


# Testing a class is very similar to testing a function but with a few differences

class AnonymousSurvey():
	"""Collect anonymous answers to a survey question."""

	def __init__(self, question):
		"""Store a question, and prepare to store responses"""
		self.question = question
		self.responses = []

	def show_question(self):
		print(self.question)

	def store_response(self, new_response):
		self.responses.append(new_response)

	def show_results(self):
		"""Show all responses that have been given"""
		print("Survey results:")
		for response in self.responses:
			print(f"- {response}")

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

my_survey.show_results()


#Testing the AnonomousSurvey class
import unittest

class TestAnonymousSurvey(unittest.TestCase):
	def test_store_single_response(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)

	def test_store_three_responses(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
	unittest.main()

# Above testing are a bit repetitive - can be made more efficient:
-------------------------------------------------------------------------
# The setUp() Method
# unittest.TestCase has a setUp() method - allows you to create these objects once and then use
# them in each of your test methods
# when included, Python runs the setUp() method before running each methos starting with test_
# any objects created in the setUp() method are then available in each test method you write

import unittest

class TestAnonymousSurvey(unittest.TestCase):

	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
	unittest.main()