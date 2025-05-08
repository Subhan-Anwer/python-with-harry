# Write a program to make a copy of a text file “this. txt”

with open("this.txt") as f:
    data = f.read()
    
with open("this_copy.txt", "w") as c:
    c.write(data)