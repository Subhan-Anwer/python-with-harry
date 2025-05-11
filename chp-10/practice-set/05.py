# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seat) and get fare information of train running under Indian Railways.
import random

class Train:
    def __init__(self, passenger_name):
        self.name = passenger_name
        
    def book_ticket(self, go_from, go_to):
        self.seat_nmbr = random.randrange(1, 100)
        self.go_from = go_from
        self.go_to = go_to
        print(f"Hello {self.name}! Your Ticket has been book from {go_from} to {go_to}, and your seat number is {self.seat_nmbr}")
        
    def get_status(self):
        print(f"your seat no is {self.seat_nmbr}, you are going from {self.go_from} to {self.go_to}")
        
    def get_fare(self):
        print("Fare is 10,000/- PKR")
        
passenger1 = Train("Subhan")
print(" ")
passenger1.book_ticket("Karachi", "Canada")
passenger1.get_status()
passenger1.get_fare()