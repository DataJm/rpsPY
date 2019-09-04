print("\n")
print("-----------------------------------------------------------------------------")
print("--------------------------- Welcome -----------------------------------------")
print("\n")

import random

choices = ["rock","paper","scissors"]

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

if(computerChoice==humanChoice):
    print(" \n  OMG IT'S A TIE!")
# rock and paper
elif(computerChoice=="rock" and humanChoice=="paper"):
    print("paper > rock \n  YOU WON, HUMAN WINS!")
elif(computerChoice=="paper" and humanChoice=="rock"):
    print("paper > rock \n  YOU LOSE, COMPUTER WINS!")
# rock and scissors
elif(computerChoice=="rock" and humanChoice=="scissors"):
    print("rock > scissors \n  YOU LOSE, COMPUTER WINS!")
elif(computerChoice=="scissors" and humanChoice=="rock"):
    print("rock > scissors \n  YOU WON, HUMAN WINS!")
# paper and scissors
elif(computerChoice=="paper" and humanChoice=="scissors"):
    print("scissors > paper \n  YOU WON, HUMAN WINS!")
elif(computerChoice=="scissors" and humanChoice=="paper"):
    print("scissors > paper \n  YOU LOSE, COMPUTER WINS!")
else:
    print("ERROR                  ############################################################################################")

print("-----------------------------------------------------------------------------")
print("-------------------------------See ya !--------------------------------------")

