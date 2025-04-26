# dictionary is just like objects of typescript used to store a set of key value pair separated by comma.

marks = {
    "Subhan" : 100,
    "Talha" : 20,
    "Ayan" : 58,
    "Shubham" : 69,
    "isSubhanPassed" : True,
    "allMarks" : (100, 20, 58, 69),
}

print("Type of marks is:" , type(marks))

print("All Marks:" , marks["allMarks"])

print("is Subhan Passed:" , marks['isSubhanPassed'])