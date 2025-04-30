# Write a program to find the sum of first n natural numbers using while loop.
num = 0
for i in range(1, 11):
    # print("before:", num)
    # print(num, "+", i)
    num += i
    # print("after:",num)
    # print('---')
print("result:",num)