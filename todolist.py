# To Do List Application - 
# To do list is empty in the begining 
tasks = []
# menu of to do list -
def menu():
    print("\n******TO DO LIST******** ")
    print("1. view all tasks")
    print("2. add new task")
    print("3. update the task")
    print("4. delete the task")
    print("5. exit")

def view_tasks():
    if len(tasks) ==0:   #if no tasks are there in list
        print("NO TASKS YET....")
    else:
        print("\nYour Tasks - ")
        number = 1
        for task in tasks:
            print(str(number)+ ". " + task)
            number = number + 1

# Add a task - 
def add_task():
    new_task = input("Enter a new task - ")
    tasks.append(new_task)
    print("task added")

# Update the task - 
def update_task():
    view_tasks()
    if len(tasks) > 0 :
        task_num =int(input("Enter task number to update - "))
        if task_num>=1 and task_num <= len(tasks):
            new_task = input("Enter a new task for this task - ")
            tasks[task_num-1] = new_task
            print("your task is updated")
        else:
            print("Invalid number...")

#delete the task - 
def delete_task():
    view_tasks()
    if len(tasks) >0:
        task_num = int(input("Enter task number to delete - "))
        if task_num>0 and task_num<= len(tasks):
            removed_task=tasks.pop(task_num -1)
            print("Task " + removed_task + " deleted !")
        else:
            print("Invalid Number...")

while True:
    menu()
    ch = input("Choose an option from 1 to 5 - ")
    if ch =="1":
        view_tasks()
    elif ch=="2":
        add_task()
    elif ch =="3":
        update_task()
    elif ch =="4":
        delete_task()
    elif ch=="5":
        print("bye")
        break
    else:
        print("Enter a number between 1 and 5 ")