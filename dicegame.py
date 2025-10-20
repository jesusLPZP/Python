import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

if die1 == die2:
    if die1 == 6:
        print("Jackpot! You rolled double sixes!")
    else:
        print("You rolled doubles!")
        print("Your rolls were" , str(die1), "and", str(die2)  )

elif die1 + die2 == 7 or die1 + die2 == 11:
    print("You win!")
    print("Your rolls were" , str(die1), "and", str(die2)  )

else:
    print("You lose!")
    print("Your rolls were" , str(die1), "and", str(die2)  )

