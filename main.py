from send import send_tasks_to_your_email
from dotenv import load_dotenv
import os


tasks = []
email_sender = os.getenv('EMAIL_SENDER')
email_password = os.getenv('MY_PASSWORD')

def add_task(task):
    tasks.append(task)
    print("Task added:", task)
def show_tasks():
    print("Current Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Send Tasks to Email")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task_name = input("Enter task: ")
        add_task(task_name)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        email_address = input("Enter email address: ")
        tasks_content = "\n".join(tasks)
        send_tasks_to_your_email(email_sender, email_password, email_address, tasks_content)
        print("Tasks sent to email.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")
