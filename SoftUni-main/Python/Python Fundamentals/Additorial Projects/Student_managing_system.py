
# Dictionary to store student records
students = {}

def add_student(name, age, grade, subjects):
	students[name]={"age": age,"grade": grade,"subjects":subjects}
	
def update_student(name):
	if name in students:
		record=students[name]
		updated_age=input(" New age: ")
		if updated_age!="":
			record["age"]=updated_age
		updated_grade=input(" New grade: ")
		if updated_grade!="":
			record["grade"]=updated_grade
		updated_subjects=input(" New subjects: ").split(',')
	
		if updated_subjects!="":
			record["subjects"]=updated_subjects
		
	else:
		print(" Student doesn't exist!")
def delete_student(name):
	if name in students:
		del students[name]
		print(f" {name} deleted")
	else:
		print(" Student doesn't exist!")
	
def search_student(name):
	if name in students:
		print(f"\n Records for {name}:")
		for k, v in students[name].items():
			if not isinstance(v, list):
				print(f" {k}: {v}")
			else: 
				print(f" {k}: ", end="")
				for i in v:
					if v.index(i)!=len(v)-1:
						print(f" {i},", end="")
					else:
						print(f" {i}", end="")
	else:
		print(" Student doesn't exist!")
	print()
def list_all_students():
	if students!={}:
		for k1, v1 in students.items():
			print(f"\n Records for {k1}:")
			for k, v in students[k1].items():
				if not isinstance(v, list):
					print(f" {k}: {v}")
			else: 
				print(f" {k}: ", end="")
				for i in v:
					if v.index(i)!=len(v)-1:
						print(f" {i},", end="")
					else:
						print(f" {i}")
	else:
		print(" No records")
	print()
def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\n Student Management System")
        print(" 1. Add Student")
        print(" 2. Update Student")
        print(" 3. Delete Student")
        print(" 4. Search Student")
        print(" 5. List All Students")
        print(" 6. Exit")
        
        # Prompt user for their choice
        choice = input(" Enter your choice: ")
        
        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")              
            if not name in students:
                age = int(input("Enter student's age: "))
                grade = float(input("Enter student's grade: "))
                subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
                add_student(name, age, grade, subjects)
            else:
                print("Student already exists!")
        elif choice == '2':
            # Prompt for student name to update
            name = input(" Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input(" Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input(" Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print(" Invalid choice, please try again.")

if __name__ == "__main__":
   main()
