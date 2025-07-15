# Q4. Write a program to filter a list of numbers which are divisible by 5.

l = []
for i in range(1, 101):
    l.append(i)
    
def div_by_5(x):
    if (x%5 == 0):
        return True
    return False

print(list(filter(div_by_5, l)))