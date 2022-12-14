print('Uchenna Library App v1.1')

# a list of the students, from the student file
def get_students(students_file):
	
	with open(students_file, 'r') as f:
		students = f.readlines()

		registered_students = []

		for student in students:
			format_student = student.strip()
			registered_students.append(format_student)
	
	return registered_students


# a list of the books, from the book file
def get_books(library_file):
	
	available_books = []

	with open(library_file, 'r') as f:
		books = f.readlines()
		
		for book in books:
			format_book = book.strip()
			available_books.append(format_book)

	return available_books


# view the currently registered students and available books in the text files.
def view_registered_students_and_books(students_list, books_list):
	""" view a formatted list of the available
	books and registered students. """
	
	view_question = input('Select from the options (1. View students | (2. View available books: ') 

	if view_question == '1': 
		for student in students_list:
			print(student)
	
	elif view_question == '2':
		for book in books_list:
			print(book)

	else: print('Please select a valid option. 1/2.')


# Add a new student to the students file.
def register_student(students_file, students_list):
	""" Append new user to file. returns updated file. """			
	
	name_request = input('Please enter your name so we can register you: ')

	if name_request.lower() not in students_list:
		with open(students_file, 'a') as f:
			print(f'Hello {name_request}. You have been added to our records.')
			f.write(name_request)
			f.write('\n')
	else:
		print(f'{name_request} is an already registered name. Please type a new one.')


# Add a new book to the library file.
def add_to_library(library_file, books_list):

	prompt = 'Enter the book title to be added: '
	book_title = input(prompt)
	
	if book_title not in books_list:
		with open(library_file, 'a') as f:
			print(f'"{book_title}" has been successfully added.\n')
			f.write(book_title)
			f.write('\n')
	else:
		print(f'{book_title} is already in our library. Please add a new book.\n')


# Make book and student enquiry
def enquire_books(borrower_file):

	with open(borrower_file, 'r') as f:
		lines = f.readlines()
		borrowed_book_and_students = []

		for line in lines:
			format_borrowed_files = line.strip().split('-')
			
			# create dict for each user borrowing book.
			student = {'book_title': format_borrowed_files[0], 'borrowed_by': format_borrowed_files[1]}
			borrowed_book_and_students.append(student)

	# View the book by title and who currently has the book.
	for info in borrowed_book_and_students:
		title = f"{info['book_title']}"
		student = f"{info['borrowed_by']}"
		print(f'Book Title: {title}\nBorrowed By: {student}\n')

	
# Ask to borrow a book here.
def check_book_availability(students_list, books_list, students_file, library_file, borrower_file):
	# Enter the book name you want to take.

	prompt_name = input('Enter your registered name: ')
	prompt_book = input('Enter the book you want to take: ')

	if prompt_name in students_list and prompt_book in books_list:
		print('Validation is Successful.')
		name_search = students_list.index(prompt_name)
		book_search = books_list.index(prompt_book)
		confirmed_student = students_list.pop(name_search)
		confirmed_book = books_list.pop(book_search)

		# update student file with removed name
		with open(students_file, 'w') as f:
			for student in students_list:
				f.write(student)
				f.write('\n')

		# update book file with removed book
		with open(library_file, 'w') as f:
			for book in books_list:
				f.write(book)
				f.write('\n')

		# append loaned book and loanee to the borrower text file.
		borrow_confirmation = f'{confirmed_book}-{confirmed_student}'
		print(f'You have taken: {borrow_confirmation}')

		with open(borrower_file, 'a') as f:
			f.write(borrow_confirmation)
			f.write('\n')
	else:		
		print('Unfortunately either your name or book is not in our files. Please check spelling etc.')
	
	
# Starts project.
def process_file():
	print('Welcome to this library file.')

	while True:
		print('\nMAIN MENU: Select your options.')
		prompt = input('1. register student\n2. check books / students\n3. add book\n4. loan enquiry\n5. Take book\n6. quit: ')

		if prompt == '1':

			students_list = get_students('students.txt')
			register = register_student('students.txt', students_list)
			continue

		elif prompt == '2':
			students_list = get_students('students.txt')
			books_list = get_books('library.txt')
			student_book_inquiry = view_registered_students_and_books(students_list, books_list)
			continue

		elif prompt == '3':
			books_list = get_books('library.txt')	
			new_book_entry = add_to_library('library.txt', books_list)
			continue

		elif prompt == '4':
			enquire = enquire_books('borrower.txt')
			continue

		elif prompt == '5':
			students_list = get_students('students.txt')
			books_list = get_books('library.txt')
			take_book = check_book_availability(students_list, books_list, 'students.txt', 'library.txt', 'borrower.txt')
			continue

		elif prompt == '6' or  prompt == 'quit':
			break

		else:
			print('\n *** ERROR *** : please enter a valid number option.\n')


# Run the project by uncommenting this file.
# start_project = process_file() 