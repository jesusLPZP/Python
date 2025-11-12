# ---------------------------------------------
# BMI Calculator Program
# Get user input for name, height and weight
# Make sure height and weight are positive
# Calculate and display BMI value and BMI category
# ---------------------------------------------

def getPositiveNumber(prompt):
    """
    Ask the user for a positive number using a while loop.
    Repeats until the user enters a value greater than 0.
    """
    value = 0
    while value <= 0:
        # Prompt the user for input
        value = float(input(prompt))
        # Check if input is positive
        if value <= 0:
            print("Please enter a positive number greater than zero.")
    return value


# --- Main Program ---
print("BMI Calculator (Python)")

# Ask for user's name
name = input("Enter your name: ")

# Get valid positive inputs for weight and height
weight = getPositiveNumber("Enter weight (lbs): ")
height = getPositiveNumber("Enter height (inches): ")
