# Exercise  ________________________________________________________
"""
    Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
    The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
    The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
"""
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
BMI = float(weight) // (float(height)**2)
print(int(BMI))
print(f"Your BMI is {BMI}")  # using f-string to print the result


"""
    I was reading this article by Tim Urban - Your Life in Weeks and realized just how little time we actually have.
    Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
    It will take your current age as the input and output a message with our time left in this format: You have x weeks left.
    Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
    Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
"""
age = input()
years = 80 - int(age)
total_weeks = years * 52

print(f"You have {total_weeks} weeks left.")
print(f"you have {total_weeks/52} years left.")
print(f"you have {round(total_weeks/12,2)} months left.")
