todo_list = []

while True:
    User_Action = input("Please select a Task from these options [Add, View, Remove, exit]: ").lower()

    if User_Action == "add":
        task = input("Enter a task: ")
        todo_list.append(task)
        print(f"The {task} task has been added")

    elif User_Action == "view":
        if not todo_list:
            print("No tasks to display.")
        else:
            print("Tasks List:")
            for idx, task in enumerate(todo_list, start=1):  # enumerate adds a counter starting from 1
                print(f"{idx}. {task}")  # Display the task with its number

    elif User_Action == "remove":
        if not todo_list:
           print("No Task To Remove")
        else:
            task = input("Enter a task: ")
            if task in todo_list:
                todo_list.remove(task)
                print(f"The {task} Task has been removed")
            else:
                print(f"The {task} Task not found to remove.")
                
    elif User_Action == "exit":
        break

    else: 
        print("Please insert a valid option")
