# Q3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table_7 = []
for i in range(1, 11):
    table_7.append(i * 7)
    
# print(table_7)

vertical_table_7 : str = ""

for i in table_7:
    vertical_table_7 += str(i) + "\n"
    
print(vertical_table_7)

# def mul_str(x):
#     return "{x}\n"
# vertical_table_7 = map(mul_str, table_7)
# print(str(vertical_table_7))