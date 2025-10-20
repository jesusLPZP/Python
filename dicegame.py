#imported the ability to choose a random number
import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
#when the two dice are the same number, the player rolls doubles

if die1 == die2:
    if die1 == 6:
        print("Jackpot! You rolled double sixes!")
    else:
        print("You rolled doubles!")
        print("Your rolls were" , str(die1), "and", str(die2)  )
#if the doubles are sixes, the player hits the jackpot

#if the sum of the two dice is 7 or 11, the player wins
elif die1 + die2 == 7 or die1 + die2 == 11:
    print("You win!")
    print("Your rolls were" , str(die1), "and", str(die2)  )
#if none of the conditions are met, the player loses
    print("You lose!")
    print("Your rolls were" , str(die1), "and", str(die2)  )

