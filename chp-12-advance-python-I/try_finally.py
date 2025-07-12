# try:
#     a = int(input("Enter a number: "))
#     print("You entered:", a)
# except Exception as e:
#     print("An error occurred:", e)
# else:
#     print("The operation was successful.")
# finally:
#     print("Hi im finally, i always run")
    


def greet(user):
    print(f"Hello {user}! whats your lucky number?")
    
    try:
        lucky_nmbr = int(input("Enter here: "))
        print(f"Ohh {user}, {lucky_nmbr} is very lucky!")
        return
    except Exception as e:
        print("An error occurred:", e)
        return
    finally:
        print(f"Bye {user}! See you next time.")
        
greet("Harry")