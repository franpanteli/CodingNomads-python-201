'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.
'''

import requests

api_endpoint_users = "http://demo.codingnomads.co:8080/tasks_api/users"
api_endpoint_tasks = "http://demo.codingnomads.co:8080/tasks_api/tasks"

user_id = input("Enter your user ID (or Task ID to view, e.g 14452): ").strip()

while True:
    print("""
Please select from the following options:
1) Quit the program
2) Create a new account (POST)
3) View all your tasks (GET)
4) View your completed tasks (GET)
5) View only your incomplete tasks (GET)
6) Create a new task (POST)
7) Update an existing task (PATCH/PUT)
8) Delete a task (DELETE)
""")
    choice = input("Enter choice (1-8): ").strip()

    if choice == "1":
        print("Goodbye!")
        break

    elif choice == "2":
        print("Creating a new account...")
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        email = input("Email: ").strip()

        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }

        response = requests.post(api_endpoint_users, json=user_data)
        if response.status_code in [200, 201]:
            print("New account created successfully!")
            print(response.json())
        else:
            print("Failed to create account:", response.text)

    elif choice in ["3", "4", "5"]:
        # Fetch the task by ID
        response = requests.get(f"{api_endpoint_tasks}/{user_id}")
        if response.status_code != 200:
            print("No task found with that ID.")
            continue

        task = response.json().get("data", {})
        if not task:
            print("No task found.")
            continue

        # Filter by completed if needed
        if choice == "4" and not task.get("completed"):
            print("No completed tasks found.")
            continue
        elif choice == "5" and task.get("completed"):
            print("No incomplete tasks found.")
            continue

        # Display the task
        status = "Completed" if task.get("completed") else "Incomplete"
        print(f"\nTask ID {task.get('id')} | {task.get('name')} [{status}]: {task.get('description')}")

    elif choice == "6":
        task_name = input("Task name: ").strip()
        task_description = input("Task description: ").strip()
        completed = input("Has the task been completed? (true/false): ").strip().lower() == "true"

        task_data = {
            "userId": int(user_id),  # The API expects userId
            "name": task_name,
            "description": task_description,
            "completed": completed
        }

        response = requests.post(api_endpoint_tasks, json=task_data)
        print("Task creation response:", response.json())

    elif choice == "7":
        task_id = input("Enter the task ID to update: ").strip()
        name = input("Updated task name (leave blank to skip): ").strip()
        description = input("Updated description (leave blank to skip): ").strip()
        completed_input = input("Update completed status? (true/false/leave blank to skip): ").strip().lower()

        update_data = {}
        if name:
            update_data["name"] = name
        if description:
            update_data["description"] = description
        if completed_input in ["true", "false"]:
            update_data["completed"] = completed_input == "true"

        response = requests.patch(f"{api_endpoint_tasks}/{task_id}", json=update_data)
        print("Update response:", response.json())

    elif choice == "8":
        task_id = input("Enter the task ID to delete: ").strip()
        response = requests.delete(f"{api_endpoint_tasks}/{task_id}")
        print("Delete response:", response.json())

    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
