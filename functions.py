import csv

from main import *

menu = {
    "1": "View list of items",
    "2": "Add an item to the list",
    "3": "update an item",
    "4": "Remove item from the list",
    "5": "Quit the program",

}
sub_menu = {
    "1": "edit the product serial number",
    "2": "Edit the product name",
    "3": "Edit the product price",
    "4": "Edit the product quantity",
    "5": "To proceed"
}

break_point = {
    "1": "Go back to the previous menu ",
    "2": "Go back to the main menu",
    "3": "Quit the program"
}

# To print the main menu


def print_menu(menu):
    print("====================")
    for key in menu:
        print(key + "-", menu[key])
    print("====================")

# Initialize choice


def user_input():
    user_input = input("Hello! Choose an option ")
    return user_input

# To View the list of ready available items


def list_of_items():

    with open("items.csv", mode="r")as read_file, open("items.csv", mode="a") as write_file:
        r = csv.reader(read_file)
        for row in r:

            print(row)
        print("Above is the list of available items")
        print("            ")

# To add an item to the list


def add_items():
    items = []
    with open("items.csv", mode="r")as read_file, open("items.csv", mode="a") as write_file:
        r = csv.reader(read_file)
        for row in r:
            items.append(row)
            print(row)
        print("These are the already existing items add new item bellow ")
    append_product = []
    append_product.append(input("key in product serial number "))
    append_product.append(input("Key in product name "))
    append_product.append(input("key in product price "))
    append_product.append(input("key in product quantity "))
    print(append_product)

    # Check befeore commit
    print("            ")
    print("====================")
    for key in sub_menu:
        print(key + " - " + " to " + sub_menu[key])
    print("====================")
    print("            ")
    print("would you like to make any changes?")

    choice = int(input("Option!  "))
    if choice == 1:
        change = input("Edit Serial number ")
        append_product[0] = change
    if choice == 2:
        change = input("Edit product name ")
        append_product[1] = change
    if choice == 3:
        change = input("Edit product Price ")
        append_product[2] = change
    if choice == 4:
        change = input("Edit product quantity ")
        append_product[3] = change
    else:
        items.append(append_product)
        file = open("items.csv", "w+", newline="")
        writer = csv.writer(file)
        writer.writerows(items)
        file.seek(0)
        Reader = csv.reader(file)
        for row in Reader:
            print(row)
        file.close()
        print("product added succesfully")

# Update an item


def update_item():
    append_product = []
    with open("items.csv", mode="r")as read_file, open("items.csv", mode="a") as write_file:
        r = csv.reader(read_file)
        for row in r:
            append_product.append(row)
            print(row)

    edit = (input(
        "select the item to edit, using the serial number"))

    for row in append_product:
        if row[0] == edit:
            print("Item Selected")
            print("                    ")
            print(row)
            print("                    ")
            print("====================")
    for key in sub_menu:
        print(key + " - " + " to " + sub_menu[key])
    print("====================")

    choice = int(input("Option!  "))
    edit = int(edit)
    go = True
    if go == True:
        if choice == 1:
            change = input("Edit Serial number ")
            append_product[edit][0] = change
            go = False
        elif choice == 2:
            change = input("Edit product name ")
            append_product[edit][1] = change
            go = False
        elif choice == 3:
            change = input("Edit product Price ")
            append_product[edit][2] = change
            go = False
        elif choice == 4:
            change = input("Edit product quantity ")
            append_product[edit][3] = change
            file = open("items.csv", "w+", newline="")
            writer = csv.writer(file)
            writer.writerows(append_product)
            file.seek(0)
            Reader = csv.reader(file)
            for row in Reader:
                print(row)
            file.close()
            print("product added succesfully")

    else:
        file = open("items.csv", "w+", newline="")
        writer = csv.writer(file)
        writer.writerows(append_product)
        file.seek(0)
        Reader = csv.reader(file)
        for row in Reader:
            print(row)
        file.close()
        print("product added succesfully")

# Delete an item


def delete_item():
    items = []
    new_items = []
    with open("items.csv", mode="r")as read_file, open("items.csv", mode="a") as write_file:
        r = csv.reader(read_file)
        for row in r:
            items.append(row)
            print(row)
        del_item = input("Chose an item to delete using the serial number ")
        for row in items:
            if row[0] == del_item:
                items.remove(row)
            for row in items:
                new_items.append(row)
                file = open("items.csv", "w+", newline="")
        writer = csv.writer(file)
        writer.writerows(items)
        file.seek(0)
        Reader = csv.reader(file)
        for row in Reader:
            print(row)
        file.close()
        print("product removed succesfully")

# Quit the program


def quit_func():
    print("Good bye!")


# Logic
start = input(
    "Hello welcome \n Y to CONTINUE to the main menun or any other key to QUIT")
if start == "Y".lower():
    run_prog = True
    while run_prog == True:
        print_menu(menu)
        user_input = input("Hello! Choose an option ")
        if user_input == "1":
            list_of_items()
        if user_input == "2":
            add_items()
        if user_input == "3":
            update_item()
        if user_input == "4":
            delete_item()
        if user_input == "5":
            print("Good Bye!")
            break
else:
    quit_func()
