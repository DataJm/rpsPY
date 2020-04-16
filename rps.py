print("\n")

print("-----------------------------------------------------------------------------")

print("--------------------------- Welcome -----------------------------------------")

print("\n")

import random

choices = ["rock","paper","scissors"]
trackComputer = []
trackHuman = []
games = 0
computerWins = 0
humanWins = 0
ties = 0
keepOn=1

while keepOn==1:
    print("\n")

    computerChoice = random.choice(choices)
    print("***********************************************************************")
    humanChoice = input("Select your weapon: rock(0), paper(1), scissors(2)")
    humanChoice = int(humanChoice)
    humanChoice = choices[humanChoice]

    print("\n ********************************")
    print(f"Computer Choice : {computerChoice}")
    print(f"Human Choice : {humanChoice}")
    print("\n ********************************")

    trackComputer.append(computerChoice)
    trackHuman.append(humanChoice)
    games += 1

    if(computerChoice==humanChoice):
        print(" \n  OMG IT'S A TIE!")
        ties += 1
    # rock and paper
    elif(computerChoice=="rock" and humanChoice=="paper"):
        print("paper > rock \n  YOU WON, HUMAN WINS!")
        humanWins += 1
    elif(computerChoice=="paper" and humanChoice=="rock"):
        print("paper > rock \n  YOU LOSE, COMPUTER WINS!")
        computerWins += 1
    # rock and scissors
    elif(computerChoice=="rock" and humanChoice=="scissors"):
        print("rock > scissors \n  YOU LOSE, COMPUTER WINS!")
        computerWins += 1
    elif(computerChoice=="scissors" and humanChoice=="rock"):
        print("rock > scissors \n  YOU WON, HUMAN WINS!")
        humanWins += 1
    # paper and scissors
    elif(computerChoice=="paper" and humanChoice=="scissors"):
        print("scissors > paper \n  YOU WON, HUMAN WINS!")
        humanWins += 1
    elif(computerChoice=="scissors" and humanChoice=="paper"):
        print("scissors > paper \n  YOU LOSE, COMPUTER WINS!")
        computerWins += 1
    else:
        print("ERROR                  ############################################################################################")
    print(f''' =========================================
        \n Overall results: 
        \n Total Games: {games} 
        \n Computer wins: {computerWins} ({(computerWins / games) * 100 } %) 
        \n Computer choices: {trackComputer} 
        \n Human wins: {humanWins} ({(humanWins / games) * 100}%) 
        \n Human choices: {trackHuman}
        \n Ties: {ties}\n''')
    keepOn=int(input("Continue? : (0)no, (1)yes"))

print("-----------------------------------------------------------------------------")
print("-------------------------------See ya !--------------------------------------")

