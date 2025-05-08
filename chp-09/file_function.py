# using w mode to write a file


file = open("my_file.txt", "w")


# writing to the file

file.write("Twinkle twinkle little stars\n")
file.write("How i wonder what you are\n")
file.write("Up above the world so high\n")
file.write("Like a diamond in the sky\n")


# closing the file
file.close()