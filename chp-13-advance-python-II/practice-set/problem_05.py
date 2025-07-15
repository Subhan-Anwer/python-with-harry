# Q5. Write a program to find the maximum of the numbers in a list using the reduce function.

nums = [1, 3, 3, 4, 5, 45, 7, 8, 9, 10]

from functools import reduce

max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num) 