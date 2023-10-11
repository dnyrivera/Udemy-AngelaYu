"""
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
86 is even because 86 ÷ 2 = 43
43 does not have any decimal places. Therefore the division is clean.

59 is odd because 59 ÷ 2 = 29.5
29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
6 ÷ 2 = 3 with no remainder.
therefore: 6 % 2 = 0

5 ÷ 2 = 2 x 2 + 1, remainder is 1.
therefore: 5 % 2 = 1

14 ÷ 4 = 3 x 4 + 2, remainder is 2.
therefore: 14 % 4 = 2
"""
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
BMI Chart

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Important: you do not need to round the result to the nearest whole number. It's fine to print out a floating point number for this exercise. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
"""

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

BMI = weight / (height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI:.1f}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI:.1f}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI:.1f}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI:.1f}, you are obese.")
else:
    print(f"Your BMI is {BMI:.1f}, you are clinically obese.")


"""
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.

This is how you work out whether if a particular year is a leap year.on every year that is divisible by 4 with no remainder except every year that is evenly divisible by 100 with no remainder unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using this flow chart .

e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)

So the year 2100 is not a leap year.
"""
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
