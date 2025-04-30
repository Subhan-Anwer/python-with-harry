# Write a program to find whether a given number is prime or not.

from simple_chalk import red, green

num = int(input("Check if its a Prime Number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        print(red(f"No! {num} is not a prime number"))
        is_prime = False
        break


if is_prime :
    print(green(f"Yes! {num} is a prime Number"))

