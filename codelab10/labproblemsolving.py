#the user will input a number and the number will now hold that value
number =  int(input("Enter a number to have a multiplication table all the way till 10: "))
for count in range(1,11):
    #kept the range from 1 to 11 because the number will always end one before the last valueof the range
    product = number * count
    #adding a "product" value by muliplying the number the user typed in by the number of the count which is increasing by one till 10
    print(f"{number} x {count} = {product}")
    #prints out the multiplication table of the number the user typed in