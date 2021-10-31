FILE = "mysquad.txt"
team_name = "plus"
team = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", 
        "Zlatan Ibrahimovic", "Ronaldinho", "Robert Lewandowski"]
msg = f"My favorite Football team is: {team_name}\n"
counter = 1
increment = 2

with open(FILE, "w") as fileWritter:
    fileWritter.write(msg)
    for player in team[::-1]:
        fileWritter.write(f"{counter} ==> {player}\n")
        counter += increment
