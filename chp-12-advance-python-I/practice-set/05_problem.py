user_num = int(input("Enter a number: "))

with open(f"table_of_{user_num}.txt", "w") as file:
    for i in range(1,11):
            file.write(f"{user_num} x {i} = {user_num*i}")
            if i < 10:
                file.write("\n")
            else:
                file.write(" ")
        

# [print(f"{user_num} x {i} = {user_num * i}") for i in range(1, 11)]