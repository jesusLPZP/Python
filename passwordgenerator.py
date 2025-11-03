import random
#list of letters to choose from
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]
#empty string to hold the password
letter = ""
#ask the user for the length of the password
length = int(input("How long do you want your password to be?" ))
#ask the user for the number of passwords to generate
quantity = int(input("How many passwords do you want?" ))
#outer loop to generate the number of passwords
for i in range(quantity):
    #inner loop to generate each password
    for i in range(length):
        #choose a random letter from the list
        letter2 = random.choice(letter_list)
        #add the letter to the password
        letter = letter + letter2
        #after the inner loop, print the password
    print(letter)
    #reset the password variable for the next password
    letter = ""