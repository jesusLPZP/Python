import random
rock = 1
paper = 2
scissors = 3
ties =  0 
wins = 0 
loses = 0
player1_choicep = input("do you want to play? (y/n)")
player1_choice = int(input("Player 1,Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
player2_choice = random.randint(1,3)
print(f"Player 2 chose: ",str(player2_choice))
while player1_choicep == "y"or player1_choicep == "Y":
    if player1_choice == player2_choice:
        print("It's a tie! Both players chose the same.")
        ties += 1
    elif ((player1_choice == rock and player2_choice == scissors)) or ((player1_choice == paper and player2_choice == rock)) or ((player1_choice == scissors and player2_choice == paper)):
        print ("You win!")
        wins += 1
    else :
        ((player2_choice == rock and player1_choice == scissors)) or ((player2_choice == paper and player1_choice == rock)) or ((player2_choice == scissors and player1_choice == paper))
        print("Player 2 wins!")
        loses += 1
    print(f"Total wins: {wins}, Total losses: {loses}, Total ties: {ties}")
player1_choicep = input()("do you want to play? (y/n)")
player1_choice = int(input("Player 1,Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
player2_choice = random.randint(1,3)