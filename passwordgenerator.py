import random
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
letter = ""
length = int(input("How long do you want your password to be?" ))
quantity = int(input("How many passwords do you want?" ))
for i in range(quantity):
    for i in range(length):
        letter2 = random.choice(letter_list)
        letter = letter + letter2
    letter = letter + "\n"
print(letter)