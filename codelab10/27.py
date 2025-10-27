#with this code line , it will print out all numbers that lead to the range but stop befor one, starts at 0
for count in range(0):
    #if the number in the range is positive, the program will start at zero and stop right before hitting the number entered in the range,because it counts zero as a number
    #all the numbers increases by one until it hits the number before the number in the range
    #if the number in the range is negative, the program will not print out anything because the range starts at 0 and stops before hitting the negative number
    print(count)
    #this code line will print out all numbers that lead to the range but stop before one.

#this code will start with the first number in the range but will stop one beofre the end number of the range. negative numbers will work in this range
for count in range(-2,6): 
    print(count)

#this code will start with the first number of the range, but the third number is how much the increase of incorments is
for count in range(0,10,2):
#in this case the number always stops a number before the last number of the range and if the incroment isnt the same , it will end the nuber closest to the last incroment increase.
    print(count)
