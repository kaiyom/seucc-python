import random as rm

FILE = "game-result.txt"
userTransection = []
compTransection = []
notInBtween = True

# menu
def gameScreen():
    print(" "*10, "-"*15)
    print(" "*10, "|Guessing Game|")
    print(" "*10, "-"*15)
    print(" "*10, "1.  Start Game")
    print(" "*10, "2.  Results")
    print(" "*10, "3.  Exit")

# game logic
def guess():
    user = int(input("Your guess: "))
    comp = rm.randint(1, 12)
    return user == comp

# prints the winner based on match score
def printWinner(userWins):
    print(" "*10, "-"*15)
    if userWins:
        print( " "*14, "You Win")
    else:
        print( " "*11, "Computer Wins")
    print(" "*10, "-"*15, "\n")

# storing score in a file
def storeScore():
    global userTransection
    global compTransection
    with open(FILE, "w") as fileWritter:
        fileWritter.write("User Transections: \n")
        fileWritter.write(f"{str(userTransection)}\n")

        fileWritter.write("\nComputer Transections: \n")
        fileWritter.write(f"{str(compTransection)}\n")
    userTransection = []    # resetting for next match
    compTransection = []    # resetting for next match

# game score logic
def gamePlay():
    userScore = 0
    compScore = 0
    for ignore in range(0, 10): # just repeat ten times
        if guess():
            userScore += 100
            print("Well done!")
        else:
            userScore -= 50
            compScore += 50
            print("Opps. Good luck for next turn.")
        
        userTransection.append(f"{userScore} BDT");
        compTransection.append(f"{compScore} BDT");
    
    storeScore()
    printWinner(userScore > compScore)

# reading score file
def printScore():
    with open(FILE, "r") as fileReader:
        print(fileReader.read())

# game loop
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
    
