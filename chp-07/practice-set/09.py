'''

for n = 3

* * * 
*   * 
* * * 

'''


n = int(input("Enter number to make pattern: ")) # taking input from user

for i in range(1, n+1): # starting loop from 1 to n not before n
    
    # this condition is for top and bottom border
    # if we are printing on line 1 or last line (n) it will print a star and space n times
    
    if i == 1 or i == n: 
        print("* " * n)
    
    # else it will print star on starting a ending of line making a border with empty space in between
    else:
        print("*", end="") # first prints a star on the starting left and to not make new line we say end=""
        
        
        print(" " * (n * 2 -3), end="") # then we are printing space on the base of 
        # n lets say 5, so 5 * 2 is 10 and - 3 subtracting 2 space for left and right star and theres also space after last star at line 1  and last so subtracting that 1 space also
        
        
        print("*") # and finally at last we are printing star and this time we want to print in next line and its default functionality so we are not going to write end=""