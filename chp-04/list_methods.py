

list1 = [1, 35,456,234,67,23,6,87,12,5,67, ]
print("before:", list1)

list1.insert(4, 50) # insert another value at specified index, 4 is index & 50 is value
print("insert 50:", list1)


list1.reverse()
print("reverse:", list1) # as the name says it reverses the list


list1.sort() # sorts the list in ascending order
print("sort:", list1)

list1.pop(3) # removes the value at index no specified in argument
print("pop:", list1)

list1.remove(23) # removes first occurence of argument
print("remove 23:", list1)