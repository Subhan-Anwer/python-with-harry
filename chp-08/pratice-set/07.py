# Write a python function to remove a given word from a list and strip it at the same time.
from simple_chalk import red, green

names = ["Ali", "Sara", "John", "Fatima", "Zara"]

def remove_word(name):
    
    if name.title() in names:
        
        print(green(f"'{name}' found in the list"))
        names.remove(name.title())
        print(f"Updated names list: {names}")
        
    else:
        print(red(f"'{name}' is not in the list"))

remove_word("sara")