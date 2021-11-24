class Color:
    red     = '\033[01;31m'
    green   = '\033[01;32m'
    blue    = '\033[01;34m'
    select  = '\033[01;40m'
    invert  = '\033[01;7m'
    nc      = '\033[00m'

class Couch:
    def __init__(self, couchId, name, dest, charge, time):
        self.couchId = couchId
        self.name = name
        self.dest = dest
        self.charge = charge
        self.time = time
    
    def __repr__(self):
        return f"Id: {self.couchId} Name: {self.name}"

## global variables
couchs = [
        Couch(1203, "Bonolota\t", "Dhaka to Rajshahi", 550, "09:15"),
        Couch(1201, "Rajdhani Express", "Rajshahi to Dhaka", 750, "08:30"),
        Couch(1205, "Snigdha\t\t", "Dhaka to Chittagong", 620, "11:30"),
        Couch(1206, "Snigdha\t\t", "Dhaka to Comilla", 450, "11:30"),
        Couch(1208, "Shovan\t\t", "Dhaka  to Sylhet", 680, "12:30"),
        Couch(1209, "Snigdha\t\t", "Comilla to Dhaka", 450, "14:30"),
        Couch(1211, "Shovan\t\t", "Sylhet  to Dhaka", 680, "17:30")
    ]
_c = Color()

def mainMenu():
    options = [
        'Reserve a Ticket',
        'View all available Trains',
        'Exit'
    ]
    print(_c.blue + "\n+" + 23*"-"+"+")
    print('|\tBD Railway\t|')
    print("+" + 23*"-"+"+" + _c.nc)
    n = 1
    for k in options:
        print(f'{n} -> {k}')
        n += 1

def printCouch():
    print("\nCouch Id\tName\t\t\tDestination\t\tCharge\tTime")
    print(40*"- ")
    for c in couchs:
        print(f"{c.couchId}\t\t{c.name}\t{c.dest}\t{c.charge}\t{c.time}")

def findCouch(couchs, couchId):
    for ch in couchs:
        if ch.couchId == couchId:
            return ch
    return None

def reserveTicket():
    name = input("Enter your name:> ")
    sit = int(input("Enter number of sit:> "))
    printCouch()
    couchId = int(input("\nEnter couch number:> "))
    couch = findCouch(couchs, couchId)
    
    if couch == None:
        print(_c.red+"**Wrong couch selected**"+_c.nc)
        return
    
    print("+"+8*"-"+"+")
    print("| Ticket |")
    print("+"+8*"-"+"+")

    print(f"Name:\t\t\t{name}")
    print(f"Number of Seats:\t{sit}")
    print(f"Couch Number:\t\t{couchId}")
    print(f"Train:\t\t\t{couch.name}")
    print(f"Destination:\t\t{couch.dest}")
    print(f"Departure:\t\t{couch.time}")
    print(f"Charges:\t\t{couch.charge*sit} Taka(BDT)")

    yn = input("\nConfirm Ticket (y/n):> ")
    if yn.lower() == 'y':
        print(_c.red+"**Reservation Done**"+_c.nc)
    else:
        print(_c.red+"**Reservation Canceled**"+_c.nc)

if __name__ == "__main__":

    while(True):
        mainMenu()
        select = int(input("Select: "))
        
        if select > 3 or select < 1:
            print(_c.red+"** Wrong option selected **"+_c.nc)
            continue
        if select == 1: 
            reserveTicket()
        if select == 2:
            printCouch()
        if select == 3:
            break
    print("Good Bye.. .")

