from random import randint # "random" is a library while randint help randomize an integer

print("Pleae choose Rock - Scissors - Paper (choose only 1):")
player = input()
computer = randint(0,2) # "computer" variable's value is randomized from 0 to 2

if computer == 0:
    computer = "Rock"
if computer == 1:
    computer = "Paper"
if computer == 2:
    computer = "Scissors"

print("----------")
print("Your choice: " + player)
print("Computer's choice: " + computer)
print("----------")

if player == computer:
    print("Draw! :|")
else:
    if player == "Rock":
        if computer == "Paper":
            print("You lose! :(")
        else:
            print("You are the winner! :D")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! :(")
        else:
            print("You are the winner! :D")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! :(")
        else:
            print("You are the winner! :D")
    else:
        print("Invalid value! :(")