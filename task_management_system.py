import json
from datetime import datetime


def check_for_valid_task_id(property_value):
    """
    Validates if the provided task ID is valid.

    Parameters:
        property_value(str): the provided value for the id property

    Returns:
        bool: whether the format of the property is correct
    """

    valid_format = True
    try:
        if not int(property_value):
            valid_format = False
    except ValueError:
        valid_format = False

    if not valid_format:
        print(f'''The provided value {property_value} for the task id is invalid.
It should contain numbers only.''')

    return valid_format


def check_for_valid_task_priority(property_value):
    """
    Validates if the provided task priority is one of low, medium or high.

    Parameters:
        property_value(str): the provided value for the priority property

    Returns:
        bool: whether the format of the property is correct
    """

    valid_format = True
    if property_value not in ['low', 'medium', 'high']:
        valid_format = False

    if not valid_format:
        print(f'''The provided value {property_value} for the task priority is invalid.
It should be one of low, medium or high.''')

    return valid_format


def check_for_valid_task_deadline(property_value):
    """
    Validates if the provided task deadline is one of a valid format.

    Parameters:
        property_value(str): the provided value for the deadline property

    Returns:
        bool: whether the format of the property is correct
    """

    valid_format = True
    try:
        if not datetime.strptime(property_value, '%Y-%m-%d'):
            valid_format = False
    except ValueError:
        valid_format = False

    if not valid_format:
        print(f'''The provided value {property_value} for the task deadline is invalid.
It should be in the format YYYY-MM-DD.''')

    return valid_format


def check_task_existence(tasks, task_id):
    """
    Check if a task with a given ID exists within the tasks list

    Parameters:
    tasks (list of dict): The current list of tasks
    task_id (str): The task which existence is being validated

    Return:
    bool: True if the task id of interest exists, False otherwise
    """

    valid_task_id = False
    for t in tasks:
        if t['id'] == int(task_id):
            valid_task_id = True

    return True if valid_task_id else False


def get_task_index(tasks, task_id):
    """
    Returns the index of the task with id = task_id within the tasks lists

    Parameters:
    tasks (list of dict): The current list of tasks
    task_id (int): The task which index will be identified

    Returns
    int: The index of the task with id = task_id
    """

    idx = None
    if check_task_existence(tasks, task_id):
        for t in tasks:
            if t['id'] == task_id:
                idx = tasks.index(t)
    else:
        print(f'There is no task with ID {task_id}')

    return idx


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.
    """

    valid_id = check_for_valid_task_id(task['id'])
    valid_priority = check_for_valid_task_priority(task['priority'])
    valid_deadline = check_for_valid_task_deadline(task['deadline'])

    if valid_id and valid_priority and valid_deadline:
        task['id'] = int(task['id'])
        tasks.append(task)
        print('Task was added successfully')
    else:
        print('Please retry with providing valid properties')
    return tasks


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    """

    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)
        tasks.pop(idx)
    else:
        print('The task you are trying to remove does not exist!')

    return tasks


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    """

    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)

        valid_priority = check_for_valid_task_priority(updated_task['priority'])
        valid_deadline = check_for_valid_task_deadline(updated_task['deadline'])

        if valid_priority and valid_deadline:
            tasks[idx]['priority'] = updated_task['priority']
            tasks[idx]['description'] = updated_task['description']
            tasks[idx]['deadline'] = updated_task['deadline']
            print('Task was added successfully')
        else:
            print('Please provide valid trask properties.')
    else:
        print('The task you are trying to update does not exist!')

    return tasks


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """

    task = None
    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)
        task = tasks[idx]
    else:
        print('The task you are trying to return does not exist!')

    return task


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    """

    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)
        task = tasks[idx]
        task['priority'] = priority
    else:
        print("The task which priority you are trying to update does not exist")

    return tasks


def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    """

    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)
        task = tasks[idx]
        task['deadline'] = datetime.strptime(deadline, '%Y-%m-%d')
    else:
        print("The task which deadline you are trying to update does not exist")

    return tasks


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    """

    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)
        task = tasks[idx]
        task['completed'] = True
    else:
        print("The task you want to mark as complete does not exist")

    return tasks


def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    """

    if check_task_existence(tasks, task_id):
        idx = get_task_index(tasks, task_id)
        task = tasks[idx]
        task['description'] = description
    else:
        print("The task which description you want to change does not exist")

    return tasks


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """

    tasks_with_keyword = []
    idx = None
    for t in tasks:
        if keyword in t['description']:
            idx = tasks.index(t)
            tasks_with_keyword.append(tasks[idx])

    return tasks_with_keyword


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """

    tasks_with_specified_priority = []
    for t in tasks:
        if t['priority'] == priority:
            idx = tasks.index(t)
            tasks_with_specified_priority.append(tasks[idx])

    return tasks_with_specified_priority


def filter_tasks_by_status(tasks, status):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """

    tasks_with_specific_status = []
    for t in tasks:
        if t['completed'] == status:
            idx = tasks.index(t)
            tasks_with_specific_status.append(tasks[idx])

    return tasks_with_specific_status


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """

    tasks_with_specific_deadline = []
    for t in tasks:
        if t['deadline'] == deadline:
            idx = tasks.index(t)
            tasks_with_specific_deadline.append(tasks[idx])

    return tasks_with_specific_deadline


def count_tasks(tasks):
    """
    Returns the total number of tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """

    return len(tasks)


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """

    return len([t for t in tasks if t['completed']])


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """

    return len([t for t in tasks if not t['completed']])


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """

    total = count_tasks(tasks)
    completed = count_completed_tasks(tasks)
    pending = count_pending_tasks(tasks)

    return {
        'total_tasks': total,
        'completed_tasks': completed,
        'pending_tasks': pending
    }


def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.

    Returns:
    None
    """

    with open(file_path, 'w') as tasks_file:
        tasks_file.write(json.dumps(tasks))


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """

    file = open(file_path, 'r')
    data = file.read()
    tasks = json.loads(data)
    file.close()

    return tasks

def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """

    sorted_tasks = sorted(tasks, key=lambda d: d['deadline'])

    return sorted_tasks


def sort_tasks_by_priority(tasks):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """

    sorted_tasks = sorted(tasks, key=lambda d: ['low', 'medium', 'high'].index(d['priority']))

    return sorted_tasks


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = {
                'id': input("Enter task ID: "),
                'description': input("Enter task description: "),
                'priority': input("Enter task priority (low, medium, high): "),
                'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                'completed': False
            }
            tasks = add_task(tasks, task)
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            tasks = remove_task(tasks, task_id)
            print("Task removed successfully.")
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            updated_task = {
                'description': input("Enter new task description: "),
                'priority': input("Enter new task priority (low, medium, high): "),
                'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
            }
            tasks = update_task(tasks, task_id, updated_task)
        elif choice == '4':
            task_id = int(input("Enter task ID to get: "))
            task = get_task(tasks, task_id)
            print("Task details:", task)
        elif choice == '5':
            task_id = int(input("Enter task ID to set priority: "))
            priority = input("Enter new priority (low, medium, high): ")
            tasks = set_task_priority(tasks, task_id, priority)
        elif choice == '6':
            task_id = int(input("Enter task ID to set deadline: "))
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks = set_task_deadline(tasks, task_id, deadline)
            print("Task deadline set successfully.")
        elif choice == '7':
            task_id = int(input("Enter task ID to mark as completed: "))
            tasks = mark_task_as_completed(tasks, task_id)
            print("Task marked as completed.")
        elif choice == '8':
            task_id = int(input("Enter task ID to set description: "))
            description = input("Enter new description: ")
            tasks = set_task_description(tasks, task_id, description)
            print("Task description set successfully.")
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.")
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.")
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
