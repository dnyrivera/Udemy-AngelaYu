# IF / ELSE STATEMENT___________________________________________________
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# IF / ELIF / ELSE STATEMENT______________________________________________
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18:
        print("Please pay $12.")
    elif age >= 12 and age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $5.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# MULTIPLE IF STATEMENT________________________________________________________
print("Welcome to the rollercoaster!")
photo_price = 3
total_bill = 0
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18:
        total_bill = 12
        print("Adult tickets are $12.")
    elif age >= 12 and age <= 18:
        total_bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        total_bill = 5
        print("Child tickets are $5.")

    wants_photo = input("Do you want a photo taken (Y/N)?").upper()
    if wants_photo == "Y":
        total_bill += photo_price
        print(f"Your final bill is ${total_bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
