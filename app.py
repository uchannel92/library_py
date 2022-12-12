# The program supposed to register Students in a file and the Books of the library in another file. 
# When a student wants to borrow a book from the library, it copy the student name from the Students file, and the book from
# the Book files and register them in Borrower file.
# The program should allow to inquiry for a specific borrower and the book he/she borrowed

# Break it down into smaller and smaller pieces.
# So, your assignment is basically:
# Get data from file
# search data
# Output data to file.

# register student to the text file.
# if the name is already registered, name is rejected. Prompy to type a new name.
def register_student(filename, view_students):
	""" Append new user to file.
		returns updated file. """			
	#filename = 'students.txt'
	
	prompt = 'Please enter your name so we can register you: '
	name_request = input(prompt)

	if name_request.lower() not in view_students:
		with open(filename, 'a') as f:
			print(f'Hello {name_request}. You have been added to our records.')
			f.write(name_request)
			f.write('\n')
	else:
		print(f'{name_request} is an already registered name. Please type a new one.')

	return filename
	
# Append book title to 'library' file
def add_book(book_filename, view_library):
	""" Add book to file """

	prompt = 'Enter the book title to be added: '
	book_title = input(prompt)
	
	if book_title not in view_library:
		with open(book_filename, 'a') as f:
			print(f'"{book_title}" has been successfully added.')
			f.write(book_title)
			f.write('\n')
	else:
		print(f'{book_title} is already in our library. Please add a new book.')


# View available books in library
def view_library(book_filename):
	""" Using for loop. """

	library = []
	
	with open(book_filename, 'r') as f:
		books = f.readlines()
		print(f'Please browse the {len(books)} books we have available: ')

		for book in books:
			format_book = book.strip()
			library.append(format_book)

	print(library)
	return library


# View the registered students.
def view_registered_students(students_file):
	""" add registered students to list """

	registered_students = []

	with open(students_file, 'r') as f:
		students = f.readlines()

		for student in students:
			format_student = student.strip()
			registered_students.append(format_student)

	print(registered_students)
	return registered_students


def check_book_availability(book_filename, books_borrowed, check_available_books):

	book_search = ''

	if book_search in check_available_books:

	# Obtain the book index 
		count = 0
		for book in check_available_books:
			if book == book_search:
				book_index = count
			else:
				count += 1

		book_to_take = check_available_books.pop(book_index)
		print(book_to_take)
		print(check_available_books)
		print(f'{book_to_take} has been removed!')

	# Move the book to take in the borrower file
		with open(books_borrowed, 'a') as f:
			f.write(book_to_take)
			f.write('\n')

	# With the removed book, rewrite the library books again with the remaining books.
		with open(book_filename, 'w') as f:
			for book in check_available_books:
				f.write(book)
				f.write('\n')
		
	else:
		print('That book is not available. sorry.')

# view_students = view_registered_students('students.txt')	
#new_user = register_student('students.txt', view_students)
#view_library = view_library('library.txt')
#new_book = add_book('library.txt', view_library)


# returns a list which is library text file.
# check_available_books = view_library('library.txt')

# check_book_availability function
# my_check = check_book_availability('library.txt', 'borrower.txt', check_available_books)		


# When a student wants to borrow a book from the library, it copy the student name from the Students file, and the book from
# the Book files and register them in Borrower file.
# The program should allow to inquiry for a specific borrower and the book he/she borrowed

# check if book is in library.
def borrow_book(borrowed_file, check_available_books, view_students):

	# prompt what book you want to borrow
	# change prompt student to student_name
	prompt_student = input('Please enter your name: ')
	prompt_book = input('what book would you like to borrow?: ')
	
	# check if student and book is in the list.
	if prompt_book in check_available_books and prompt_student in view_students:
		print(True)
		print(f'{prompt_student} is registered, and {prompt_book} is available to borrow.')
	
		request_book = input('Would you like to take this book? (y/n): ')

		if request_book == 'y':
			borrow_confirmation = f'{prompt_book}-{prompt_student}'
			print(f'You have taken: {borrow_confirmation}')

			with open(borrowed_file, 'a') as f:
				f.write(borrow_confirmation)
				f.write('\n')
		elif request_book == 'n':
			print(f'you have decided not to take {prompt_book}')
			pass

	elif prompt_book not in check_available_books:
		print(f'{prompt_book} is not available, sorry.')
		# if the student is not there don't continue.
		print(False)
		
	elif prompt_student not in view_students:
		print(f'{prompt_student} is not registered. Please register before you can borrow books.')
	# if book is in library, pop the line. 
	# read library and pop that line from library
	# move into borrowed file
	# gather the library with the removed book, and WRITE the library again.
	
#student_request = borrow_book('borrower.txt', check_available_books, view_students)

# When a book is borrowed, add user and book to borrower text file - DONE
# The app should then go into the library file and remove the book. then reappend the list again with the removed book.

def inquire_books(borrowed_file):

	with open(borrowed_file, 'r') as f:
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


inquire_books('borrower.txt')
