import unittest

from main import get_students

class TestLibraryClass(unittest.TestCase):

# run a unittest that allows you to enter a name and confirm in the unittest the new student is in the file.

	def test_student_file(self):
		""" is michael in the student list? """

		test_get_students = get_students('students.txt')
		print(test_get_students)
		self.assertIn('michael', test_get_students)


if __name__ == '__main__':
	unittest.main()
