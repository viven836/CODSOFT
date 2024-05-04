def addtask():
    task = input("Enter a task:")
    print()
    tasks.append(task)
    print("Task added")
    for task in tasks:
        print("->", task)

    print()
   
def showtasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print(" Present Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        print("-------------------------")

        print("Completed Tasks:")
        for i, com_task in enumerate(comp_tasks, 1):
            print(f"{i}. {com_task}")
    print()

def deltask():
    print("Deleting a task:")
    if tasks:
        showtasks()
        task_index = input("Enter the number of the task to delete: ")
        try:
            index = int(task_index) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    else:
        print("No tasks to delete.")
    print()

def taskstat():
    if tasks:
        showtasks()
        task_index = input("Enter the task no to mark it complete:")
        try:
                index = int(task_index) - 1
                if 0 <= index < len(tasks):
                    com_task = tasks[index]
                    comp_tasks.append(com_task)
                    print("Task added")
                    for com_task in comp_tasks:
                        print("->", com_task)
                    del tasks[index]
                    print("Task completed successfully.")
                else:
                    print("Invalid task number.")
        except ValueError:
                print("Invalid input. Please enter a valid task number.")

    else:
        print("No tasks to completes.")
    print()

print()
print("<------TO-DO LIST----->")
tasks = []
comp_tasks = []
while True:
    print("What do you want to do?")
    print("1.Add task")
    print("2.Delete task")
    print("3.Show the tasks")
    print("4.Status of tasks")
    print("5.Exit")
    
    n =input("Enter choice:")

    match n:
        case '1':
           
            print()
            addtask()
            print()

        case '2':
           
            print()
            deltask()
            print()

        case '3':
            
            print()
            showtasks()
            print()
        
        case '4':
            
            print()
            taskstat()
            print()
       
        case '5':
            print("Exiting...")
            print()
            break

        case _:
            print("Wrong choice!")

