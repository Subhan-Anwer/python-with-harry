studentMarks = []

studentMarks.append(input("Enter Student 1 Marks: "))
studentMarks.append(input("Enter Student 2 Marks: "))
studentMarks.append(input("Enter Student 3 Marks: "))
studentMarks.append(input("Enter Student 4 Marks: "))
studentMarks.append(input("Enter Student 5 Marks: "))
studentMarks.append(input("Enter Student 6 Marks: "))

print(studentMarks) # before sorting

studentMarks.sort() # sorting

print("Ascending", studentMarks)

studentMarks.reverse()
print("Descending", studentMarks)
