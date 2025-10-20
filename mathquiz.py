import random
# 1. Generate two random single-digit integers (0–9)
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
#chooses a random number and are listed as special variables 

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
   temp = number1
   number1 = number2
   number2 = temp
#swaps the numbers to avoid negative answers if the second number is larger than the first

# 3. Prompt the student to answer "What is number1 - number2?"
answer = int(input(f"What is {number1} - {number2}? "))
#takes the user's answer as an integer input

# 4. Grade the answer and display the result
if number1 - number2 == answer:
   print("You are correct!")
else:
   print("Your answer is wrong.")
   print(f"{number1} - {number2} should be {number1 - number2}.")
