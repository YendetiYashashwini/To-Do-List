tasks = []
def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f'Task "{task}" added successfully!')
def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed successfully!\n')
    else:
        print("Task not found!\n")
def view_tasks():
    if tasks:
        print("Your To-Do List: \n")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    else:
        print("Your To-Do List is Empty!\n")
while True:
    print("To-Do List Menu: ")
    print("1. Add Task")                    
    print("2. Remove Task")                    
    print("3. View Tasks")  
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()  
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the To-Do List Application! Thank You!")
        break
    else:
        print("Invalid choice! Please select a valid choice between 1 to 4.")
        continue                      
