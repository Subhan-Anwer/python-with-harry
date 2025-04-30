'''

n = 3
  *
 ***
*****


n = 5
    *
   ***
  *****
 *******
*********

'''



n = int(input("Enter number to make pattern: "))


for i in range (1 , n+1):
    print(" " * (n-i), end="")
    print("*" * (2 * i - 1) )