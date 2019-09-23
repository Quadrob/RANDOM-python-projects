# A function, denoted by def is a re-usable block of code that that can be called to perform
# repetitive tasks. This task can be to return a value of a calculation or any other value, or
# it could perform an operation on the internal state of the program such as change the contents
# of a text file, variable(Particularly a data structure)
# ===
# functions can also take parameters, and when the function  is called, it can take the passed variable/value
# as input. Notice that to call a function you simply say function_name(optional parameters goes here)
# An example of a typical function call is average(1, 2, 3) which returns and/or prints 2. The internal
# workings of the function will add the numbers and divide it by 3, but all of that is abstracted away
# with the use of a function :)


def print_numbers(numbers): # Function that seems to take a dictionary as a parameter
    print("Telephone Numbers:")
    for x in numbers.keys(): # Iterates over keys in dictionary, meaning x is the value.
        print("Name:", x, "\tNumber:", numbers[x])
    print

def add_number(numbers, name, number): # Function that takes in the same dictionary, and adds the key-value pair of name and number passed to the function.
    numbers[name] = number #

def lookup_number(numbers, name): # Function that returns the number by using the name as the access key
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"

def remove_number(numbers, name):
    if name in numbers:
        del numbers[name] # Removing the key-value pair from the dictionary
    else:
        print(name," was not found")

# Here comes the IO operation functions
def load_numbers(numbers, filename):
    in_file = open(filename, "r")
    for in_line in in_file:
        in_line = in_line.rstrip('\n')    #Remove next line characters before and after each line 
        name, number = in_line.split(",") #Splits on commas
        numbers[name] = number
    in_file.close()

def save_numbers(numbers, filename):
    out_file = open(filename, "w")
    for x in numbers.keys():
        out_file.write(x + "," + numbers[x] + "\n")
    out_file.close()

def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print

phone_list = {} # A dictionary declaration
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        filename = input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()

print("Goodbye")