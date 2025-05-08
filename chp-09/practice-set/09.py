# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f1:
    f1_data = f1.read()
    
with open("this_copy.txt") as f2:
    f2_data = f2.read()

if f1_data.lower() == f2_data.lower():
    print("File_1 and File_2 is identical")
else:
    print("Both are different")