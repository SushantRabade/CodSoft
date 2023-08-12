import art

print(art.logo)
Task_list = []

def add():
    """ Adding the task here """

    add_task = input("Enter the your task : \n")
    Task_list.append(add_task)
    print("Your task is added successfully!\n")

    task_add = True
    while task_add:
        want_add = input("Do you want to add more tasks press y for yes and n for no : ").lower()
        if want_add == 'y':
            add_task = input("Enter the your task : \n")
            Task_list.append(add_task)
            print("Your task is added successfully!\n")
        else:
            task_add = False

def read():
    """ Showing the task here """

    if len(Task_list) == 0:
        print("Tasks are tasks not added\n")
    else:
        i = 1
        print("Your All task are")
        for task in Task_list:
            print(f"{i}. {task}")
            i += 1
        print("\n")
def update():
    """ Updating the task here """

    read()
    task_num = int(input("Enter the number of task you want to update : "))
    update_task = task_num - 1
    add_task = input("Enter the new task: \n")
    Task_list[update_task] = add_task
    print("Your task is updated successfully!\n")

def delete():
    """ Deleting the task here """

    read()
    task_num = int(input("Enter the number of task you want to delete : "))
    update_task = task_num - 1
    Task_list.pop(update_task)
    print("Your task is deleted successfully!\n")


To_do_list = True

while To_do_list:
    print("1. Add")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    user = input("Please select number of operation : ")
    print("\n")

    if user == '1':
        add()

    elif user == '2':
        read()

    elif user == '3':
        update()

    elif user == '4':
        delete()

    elif user == '5':
        To_do_list = False

    else:
        print("Please enter the valid number of operation \n")