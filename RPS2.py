import random

rock = 1
paper = 2
scissors = 3

ties = 0
wins = 0
loses = 0

# Loop as long as the user wants to play
while True:
    player1_choicep = input("Do you want to play? (y/n): ")
    if player1_choicep.lower() != 'y':
        print(f"You chose not to continue")
        break

    # Get player choice
    player1_choice = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    player2_choice = random.randint(1, 3)

    # Show player 2's choice
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    print(f"Player 2 chose: {choices[player2_choice]}")

    # Determine outcome
    if player1_choice == player2_choice:
        print("It's a tie!")
        ties += 1
    elif ((player1_choice == rock and player2_choice == scissors) or
          (player1_choice == paper and player2_choice == rock) or
          (player1_choice == scissors and player2_choice == paper)):
        print("You win!")
        wins += 1
    else:
        print("player 2 wins")
    loses += 1

    # Show score
    print(f"Total wins: {wins}, Total losses: {loses}, Total ties: {ties}")

