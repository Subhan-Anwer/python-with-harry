# Write a program to find out the line number where python is present from ques 6.

# with open("log.txt") as f:
#     data = f.read()
    
# detector = data.count("python")
# # print(detector)
# i = 1

# while i <= int(detector):
#     with open("log.txt") as f:
#         read_line = f.readline()
#         if "python" in read_line:
#             print(f"Python found at line number {i}")
#         else:
#             (f"not found in line number {1}")
#     i += 1




# with open("log.txt") as f:
#     read_line = f.readlines()
#     # print(read_line)
    

# line_num = 1


# for line in read_line:
#     if "python" in read_line:
#         print(f"python is present at no: {line}")
    
#     else:
#         print(f"No Python is not present at: {line_num}")
    
#     line_num += 1


with open("log.txt") as f:
    read_lines = f.readlines()

linenum = 1
for currline in read_lines:
    if("python" in currline):
        print(f"Yes python is present. Line no: {linenum}")
        break
    linenum += 1

else:
    print("No Python is not present")