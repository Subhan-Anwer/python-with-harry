# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function.

from simple_chalk import chalk, green

name = input("Enter name: ")

print(green("Good Afternoon, "+name))