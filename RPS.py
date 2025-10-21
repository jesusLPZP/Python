import random
rock = 1
paper = 2
scissors = 3
player1_choice = int(input("Player 1,Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
player2_choice = random.randint(1,3)
print(f"Player 2 chose: ",str(player2_choice))

if player1_choice == player2_choice:
    print("It's a tie! Both players chose the same.")
elif (player1_choice == rock and player2_choice == scissors):
    print ("You win! Rock crushes Scissors.")
elif (player1_choice == paper and player2_choice == rock):
    print("You win! Paper covers Rock.")
elif (player1_choice == scissors and player2_choice == paper):
    print("You win! Scissors cut Paper.")
elif (player2_choice == rock and player1_choice == scissors):
    print("Player 2 wins! Rock crushes Scissors.")
elif (player2_choice == paper and player1_choice == rock):
    print("Player 2 wins! Paper covers Rock.")
else: 
    (player2_choice == scissors and player1_choice == paper)
    print("Player 2 wins! Scissors cut Paper.")

