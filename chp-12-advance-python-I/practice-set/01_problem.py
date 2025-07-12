# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

# try:
#     with open("1.txt") as file_1:
#         print("File 1 exist!")
# except FileNotFoundError:
#     print("File 1 does not exist")
    
# try:
#     with open("2.txt") as file_2:
#         print("File 2 exist!")
# except FileNotFoundError:
#     print("File 2 does not exist")
    
# try:
#     with open("3.txt") as file_3:
#         print("File 3 exist!")
# except FileNotFoundError:
#     print("File 3 does not exist")

        
i = 1

while i <= 3:
    try:
        with open(f"{i}.txt") as file:
            print(f"File {i} exist!")
    except FileNotFoundError:
        print(f"File {i} does not exist")
        
    i += 1