import re
from datetime import datetime as dt

class User:
    def __init__(self, name, dob, phNumber):
        if any([char.isdigit() for char in name]):
            raise Exception("Name is not valid")

        if not phNumber.isdigit():
            raise Exception("Phone is not valid")

        try:
            self.dob = dt.strptime(dob, "%Y-%m-%d")
        except ValueError:
            raise Exception("Date of birth is not valid")
        
        self.name = name
        self.phNumber = phNumber

    def display(self):
        print('''
        Welcome {}, You are identified as a valid user.
        Your DoB is {}, 
        and phone number is {}.
        '''.format(self.name, 
        self.dob.strftime('%A %Y-%m-%d'), self.phNumber))
        
if __name__ == "__main__":
    name = input("Enter your name:\n")
    dob = input("Enter date of birth: (yyyy-mm-dd)\n")
    phNumber = input("Enter phone number:\n")

    user1 = User(name, dob, phNumber)
    user1.display()
