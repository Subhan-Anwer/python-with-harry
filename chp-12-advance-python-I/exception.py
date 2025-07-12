# Exception is used for error handling.

# try:
#     user_number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input! Please enter a number!")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# print("Thank you for entering number!")




# print("\n ---------------------------- \n")



# Checking user lottery number

winning_number = 69

def check_user_lottery():
    
    won_lottery = False
    
    while not won_lottery:
        try:
            user_lottery_number = int(input("Enter your lottery number: "))
        except ValueError:
            print("Please Enter a Valid Number!")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

        if user_lottery_number == winning_number:
            print("Congratulations! you have won!")
            won_lottery = True
        else:
            print("Sorry, you didn't win.")
        
# Calling the function to check user's lottery number
check_user_lottery()