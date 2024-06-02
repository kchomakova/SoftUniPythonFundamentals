# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    """
    The function adds a new student record.

    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.

    Return value: None
    """

    students[name] = {'age': age, 'grade': grade, 'subjects': subjects}
    print('Added the following student to the students database')
    print(f'Name: {name}, Age: {age}, Grade: {grade}, Subjects: {subjects}')


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.

    Return value: None
    """

    if name not in students:
        raise Exception('The student you are trying to update does not exist!')

    print('''Select the student\'s attribute you want to update.
    Attributes that can be updated are: age, grade, subjects''')
    attr = input()
    print('You are trying to update the information about the following student:')
    print(f'{name}: {students[name]}')

    if attr == 'age':
        new_age = input('Please enter the new value for the age (whole number) ...')
        if new_age:
            students[name]['age'] = int(new_age)
    elif attr == 'grade':
        new_grade = input('Please enter the new value for the grade (decimal) ...')
        if new_grade:
            students[name]['grade'] = float(new_grade)
    elif attr == 'subjects':
        new_subjects = input('Please enter the new value for the subjects (comma-separated) ...')
        if new_subjects:
            students[name]['subjects'] = new_subjects.split(',')
    else:
        raise Exception('The attribute you are trying to update does not exist!')

    print('The updated information about the student is as follows:')
    print(f'{name}: {students[name]}')

def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.

    Return value: none
    """

    if name in students:
        print(f'Deleting the following student: {name}: {students[name]}')
        del students[name]
    else:
        raise Exception('The student you are trying to delete does not exist!')


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.

    Return value: None
    """
    if not students[name]:
        raise Exception('The student you are trying to find does not exist!')
    else:
        print(f'The details about the student {name} are: {students[name]}')


def list_all_students():
    """
    List all student records.

    Return value: None
    """

    if not students:
        raise Exception('There are no students in the students database')
    else:
        print(f'Students are: {students}')


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            max_retries = 3
            retries = 0
            while retries < max_retries:
                retries += 1
                # Prompt for student details
                try:
                    name = input("Enter student's name: ")
                    age = int(input("Enter student's age: "))
                    grade = float(input("Enter student's grade: "))
                    subjects = input("Enter student's subjects (comma-separated): ").split(',')
                except ValueError as e:
                    print('An exception occurred:', e)
                    print('Please try again...')
                    continue
                else:
                    # Call the add_student function
                    add_student(name, age, grade, subjects)
                    break
            else:
                print('You have reached the maximum number of attempts to provide valid attributes.')
                break
        elif choice == '2':
            max_retries = 3
            retries = 0
            while retries < max_retries:
                retries += 1
                # Prompt for student name to update
                name = input("Enter student's name to update: ")

                try:
                    # Call the update_student function
                    update_student(name)
                except (ValueError, Exception) as e:
                    print('An exception occurred:', e)
                    if retries < max_retries:
                        print('Please try again...')
                    continue
                else:
                    break
            else:
                print('You have reached the maximum number of attempts to provide a valid name.')
                break
        elif choice == '3':
            max_retries = 3
            retries = 0
            while retries < max_retries:
                retries += 1
                # Prompt for student name to delete
                name = input("Enter student's name to delete: ")
                try:
                    # Call the delete_student function
                    delete_student(name)
                except (ValueError, Exception) as e:
                    print('An exception occurred:', e)
                    if retries < max_retries:
                        print('Please try again...')
                    continue
                else:
                    break
            else:
                print('You have reached the maximum number of attempts to provide a valid name.')
                break
        elif choice == '4':
            max_retries = 3
            retries = 0
            while retries < max_retries:
                retries += 1
                # Prompt for student name to search
                name = input("Enter student's name to search: ")
                try:
                    # Call the search_student function
                    search_student(name)
                except (ValueError, Exception) as e:
                    print('An exception occurred:', e)
                    if retries < max_retries:
                        print('Please try again...')
                    continue
                else:
                    break
            else:
                print('You have reached the maximum number of attempts to provide a valid name.')
                break
        elif choice == '5':
            try:
                # Call the list_all_students function
                list_all_students()
            except Exception as e:
                print('An exception occurred:', e)
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
