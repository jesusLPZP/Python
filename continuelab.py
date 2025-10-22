runs = 0
user = input("do you want to continue? (y/n): ")
while user == "y" or user == "Y":
    runs += 1
    print("Do you want to continue? (y/n): ")
    user = input()
print("You chose to not continue,you played the program " +str(runs)+ "times.")