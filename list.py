
todolist = []

def ifstatements():
    global number5
    # number5 is the variable that holds what option the user picked
    if number5 == "1":
        add_item()
    elif number5 == "2":
        remove_item()
    elif number5 == "3":
        print_list()
    elif number5 == "4":
        reset_list()
    else:
        print("wrong")

def add_item():
    item1 = input("what: ")
    # what the user wants to add
    todolist.append(item1)
    show_menu()
    pass
def remove_item():
    itemr = input("whatchu wanna remove: ")
    #what the user wants to remove
    todolist.remove(itemr)
    show_menu()
    pass
def print_list():
    #look at the name
    print(todolist)
    show_menu()
    pass
def reset_list():
    todolist.clear()
    show_menu()
    pass
def show_menu():
    global number5
    print("Press 1 to add item")
    print("Press 2 to remove item")
    print("Press 3 to print list")
    print("Press 4 to reset list")
    number5 = input("Enter: ")
    ifstatements()
    # ifstatements handles all the logic
    pass

show_menu()


