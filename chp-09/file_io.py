# file = open("file.txt")
# file_data = file.read()
# print(file_data)


def write_in_file(text):
    file = open("file.txt", "r")
    file_data = file.read()
    file = open("file.txt", "w")
    file.write(file_data + "\n"  + text)
    file.close()



my_msg = "Subhan bhai is a freelance full stack developer"
write_in_file(my_msg)