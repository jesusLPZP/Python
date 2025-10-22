#stores the number of times the user tries to continue the program
runs = 0
#asks the user if they want to continue
user = input("do you want to continue? (y/n): ")
#loops the program while the user inputs y or Y
while user == "y" or user == "Y":
    runs += 1
    print("Do you want to continue? (y/n): ")
    user = input()
#prints the amount of thimes the user started the program again before typing n or anything else other then "y" or ""Y" 
print("You chose to not continue,you played the program " +str(runs)+ " times.")