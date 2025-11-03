# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

print("Welcome to the Debugging Lab!")

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")
#list of test scores
scores = [85, 90, 78, 88, 92]
#next lines of codes, it will calculate the total of all the numbers inside the list
total = 0
for score in scores:
    total = total + score
#len is used to calculate how many numebers or avriables are inside the list
average = total / len(scores)
#grabes the total value from the past line and divides it by how many numbers are inside the list to get the average
print("Your average score is:", average)
#adds new variable called highest to hold the highest score
highest = 0
#the s is used to hold the values inside the list one by one and tries to find the largets number to hold the new value for the hiest score
for s in scores:
    if s > highest:
        highest = s

print("Your highest score was:" + str(highest))