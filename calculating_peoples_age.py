# This code will store the name of the user and greet them
name = input("Enter your name:")

#This code will store the users favorite hobby
favorite_hobby = input("Enter your favorite hobby:")

# This code will store the current year the user types in.
current_year = int(input("Enter the current year:"))

# This code will store the user's year of birth.
year_of_birth = int(input("Enter your year of birth:"))

# This code will calculate the user's current age.
current_age = current_year - year_of_birth

#This code will print out the user's name, age, and favorite hobby.
print(f"I, {name}, I am {current_age} and I spend my free time by {favorite_hobby} ")