# by defining katz_deli list inside the class, we can encapsulate the data( variables and functions).These are not globally accessible.

katz_deli = []


def line(deli_list):
    if len(deli_list) == 0:
        print("The line is currently empty.")
    else:
        line_string = "The line is currently:"
        for index, name in enumerate(deli_list, 1):
            line_string += f" {index}. {name}"
        print(line_string)

def take_a_number(katz_deli, name):
    #accepts two args, list for the current line of ppl, and string for the joining person 
    #count from 1 
    #print() Welcome, {name}. You are number ... in line"
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")



def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)


line([])
line(["Logan","Avi","Spencer"])
