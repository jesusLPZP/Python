import random
rock = 1
paper = 2
scissors = 3
player1_choice = int(input("Player 1,Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
player2_choice = int(input("Player 2 ,Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
if player1_choice == player2_choice:
    print("It's a tie!")
elif (player1_choice == rock and player2_choice == scissors):
    print ("You win! Rock crushes Scissors.")
elif (player1_choice == paper and player2_choice == rock):
    print("You win! Paper covers Rock.")
elif (player1_choice == scissors and player2_choice == paper):
    print("You win! Scissors cut Paper.")
else:
    print("You lose!")

