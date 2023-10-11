# Project - Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(
    input("What percentage tip would you like to give?[10, 12, or 15]? "))
people = int(input("How many people to split the bill? "))

total_bill_plus_tip = bill * (1 + tip / 100)
value_per_person = total_bill_plus_tip / people

final_amount = round(value_per_person, 2)

print(f"Each person should pay: ${final_amount}")
print(f"Each person should pay: ${value_per_person:.2f}")
