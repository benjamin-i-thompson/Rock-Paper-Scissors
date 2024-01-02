import random as r
import tkinter as tk

flag = True
while (flag == True):

    userIn = input("Rock, Paper, or Scissors? (press 'q' to quit) ")
    if (userIn == 'q'):
        flag = False

    else:
        def computerInpt(num):
            if (num == 1 or num == 4):
                comp = "rock"
            elif (num == 2 or num == 5):
                comp = "paper"
            else:
                comp = "scissors"
            return comp

        def compare(u, c):
            if (u == c):
                return "Tie"
            elif ((u == 'rock' and c == 'paper') or (u == 'paper' and c == 'scissors') or (u == 'scissors' and c == 'rock')):
                return "You Lose!"
            else:
                return "You Win!"

        compIn = computerInpt(r.randint(1,6))
        print(f"Your input: {userIn}")
        print(f"Computer picked: {compIn}")

        print(compare(userIn.lower(), compIn))
