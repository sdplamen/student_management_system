# Dictionary to store student records
students = {}

def add_student(name, age, grade, subjects):
	"""
	Add a new student record.
	Args:
	- name (str): The name of the student.
	- age (int): The age of the student.
	- grade (float): The grade of the student.
	- subjects (list of str): The subjects the student is enrolled in.
	"""
# Code to add a new student record
	if name in students:
		print(f'Student {name} already exists.')
	students[name] = {
		'age': age,
		'grade': grade,
		'subjects': subjects
	}
	print(f'Student {name} added successfully.')

def update_student(name):
	"""
	Update an existing student record.
	Args:
	- name (str): The name of the student whose record is to be updated.
	"""

# Check if the student exists
# Prompt the user to update fields and keep current values if fields are empty
# Code to update the student's record
	if name in students:
		print(f'Updating student {name}. Leave blank to keep the current value.')
		age = input(f'Enter student\'s new age (current: {students[name]["age"]}): ')
		grade = input(f'Enter student\'s new grade (current: {students[name]["grade"]}): ')
		subjects = input(f'Enter student\'s new subjects (current: {", ".join(students[name]["subjects"])}): ')

		if age:
			students[name]['age'] = int(age)
		if grade:
			students[name]['grade'] = float(grade)
		if subjects:
			students[name]['subjects'] = subjects.split(',')
		print(f'Student {name} updated successfully.')
	else:
		print(f'Student {name} not found.')

def delete_student(name):
	"""
	Delete a student record based on the student's name.
	Args:
	- name (str): The name of the student to delete.
	"""

# Check if the student exists
# Code to delete the student's record
	if name in students:
		del students[name]
		print(f'Student {name} deleted successfully.')
	else:
		print(f'Student {name} not found.')

def search_student(name):
	"""
	Search for a student by name and return their record.
	Args:
	- name (str): The name of the student to search for.
	"""

# Check if the student exists
# Code to return the student's record
	if name in students:
		print(f'Details for student {name}:\nAge: {students[name]["age"]}\nGrade: {students[name]["grade"]}\nSubjects: {", ".join(students[name]["subjects"])}')
	else:
		print(f'Student {name} not found.')
def list_all_students():
	"""
	List all student records.
	"""

# Check if there are any student records
# Code to list all students
	if students:
		for name, details in students.items():
			print(f'Name: {name}\nAge: {details["age"]}\nGrade: {details["grade"]}\nSubjects: {", ".join(details["subjects"])}')
	else:
		print('No students found.')

def main():
	"""
	Main function to provide user interaction.
	"""
	while True:
		# Display menu options
		print('\nStudent Management System')
		print('1. Add Student')
		print('2. Update Student')
		print('3. Delete Student')
		print('4. Search Student')
		print('5. List All Students')
		print('6. Exit')

		# Prompt user for their choice
		choice = input('Enter your choice: ')

		if choice == '1':
			# Prompt for student details
			name = input('Enter student\'s name: ')
			age = int(input('Enter student\'s age: '))
			grade = float(input('Enter student\'s grade: '))
			subjects = input('Enter student\'s subjects (comma-separated): ').split(',')
			# Call the add_student function
			add_student(name, age, grade, subjects)
		elif choice == '2':
			# Prompt for student name to update
			name = input('Enter student\'s name to update: ')
			# Call the update_student function
			update_student(name)
		elif choice == '3':
			# Prompt for student name to delete
			name = input('Enter student\'s name to delete: ')
			# Call the delete_student function
			delete_student(name)
		elif choice == '4':
			# Prompt for student name to search
			name = input('Enter student\'s name to search: ')
			# Call the search_student function
			search_student(name)
		elif choice == '5':
			# Call the list_all_students function
			list_all_students()
		elif choice == '6':
			# Exit the program
			break
		else:
			print('Invalid choice, please try again.')


if __name__ == '__main__':
	main()