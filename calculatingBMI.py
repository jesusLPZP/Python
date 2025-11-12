# ----------------------------------------------------------
# Program: BMI Calculator
# Description:
#   This program asks the user for their name, weight (in lbs),
#   and height (in inches). It calculates their Body Mass Index (BMI)
#   using a standard formula and displays the BMI value along with
#   a weight category such as Underweight, Normal, Overweight, or Obese.
# ----------------------------------------------------------


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


def calculateBMI(weightPounds, heightInches):
    """
    Calculate  BMI = (weightPounds / heightInches^2) * 703
    Return the BMI value based on weight (lbs) and height (inches).     
    """
    bmi = (weightPounds / (heightInches * heightInches)) * 703
    return bmi


def getCategory(bmi):
    """
    Determine the BMI category based on value.
    """
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return category


# --- Main Program ---
print("BMI Calculator (Python)")

# Ask for user's name
name = input("Enter your name: ")

# Get valid positive inputs for weight and height
weight = getPositiveNumber("Enter weight (lbs): ")
height = getPositiveNumber("Enter height (inches): ")

# Calculate BMI and determine category
bmiValue = calculateBMI(weight, height)
category = getCategory(bmiValue)

# Display results
print()
print(name, "your BMI is", round(bmiValue, 1), "(", category, ")")

