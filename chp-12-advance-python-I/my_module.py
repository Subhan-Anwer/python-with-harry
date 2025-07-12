def greet(user):
    print(f"Hello {user.title()}! whats your lucky number?")
    
    try:
        lucky_nmbr = int(input("Enter here: "))
        print(f"Ohh {user.title()}, {lucky_nmbr} is very lucky!")
        return
    except Exception as e:
        print("An error occurred:", e)
        return
    finally:
        print(__name__) # __name__ will be '__main__' when run directly and will be the file name 'my_module' in this case if imported
        print(f"Bye {user}! See you next time.")
        return
    
# greet("subhan")