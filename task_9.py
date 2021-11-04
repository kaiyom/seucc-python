import random as rm

FILE = "game-result.txt"
userTransection = []
compTransection = []
notInBtween = True

def gameScreen():
    print(" "*10, "-"*15)
    print(" "*10, "|Guessing Game|")
    print(" "*10, "-"*15)
    print(" "*10, "1.  Start Game")
    print(" "*10, "2.  Results")
    print(" "*10, "3.  Exit")

def guess():
    user = int(input("Your guess: "))
    comp = rm.randint(1, 12)
    return user == comp

def printWinner(userWins):
    print(" "*10, "-"*15)
    if userWins:
        print( " "*14, "You Win")
    else:
        print( " "*11, "Computer Wins")
    print(" "*10, "-"*15, "\n")

def gamePlay():
    userScore = 0
    compScore = 0
    for ignore in range(0, 10): # repeat ten times
        if guess():
            userScore += 100
            print("Well done!")
        else:
            userScore -= 50
            compScore += 50
            print("Opps. Good luck for next turn.")
        
        userTransection.append(f"{userScore} BDT");
        compTransection.append(f"{compScore} BDT");
    
    printWinner(userScore > compScore)

def printScore():
    with open(FILE, "w") as fileWritter:
        fileWritter.write("Your Transections: \n")
        for eachTr in userTransection:
            fileWritter.write(f"{eachTr}\n")

        fileWritter.write("\nComputer Transections: \n")
        for eachTr in compTransection:
            fileWritter.write(f"{eachTr}\n")

while True:
    if notInBtween:
        gameScreen()
        user = int(input("Enter your choice: "))
        if user == 1:
            gamePlay()
            notInBtween = False
        elif user == 2:
            printScore()
            print("Your last match score are printed in file. :)")
        else:
            print("Byyeee")
            break
    else:
        user = input("Do you want to continue the game? (y/n): ")
        if user.lower() == "y":
            gamePlay()
        else:
            notInBtween = True
