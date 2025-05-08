file = open("my_file.txt")

l1 = file.readline()
l2 =file.readline()
l3 =file.readline()
l4 =file.readline()

print(l1, end="")
print(l2, end="")
print(l3, end="")
print(l4, end="")

file.close()