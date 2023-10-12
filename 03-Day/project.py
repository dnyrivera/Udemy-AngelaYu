print("""
              ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
   hjw     /____________\
   `97     |____________|
""")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower().strip()

if direction == "left":
    print("You are save for now!")

    direction = input(
        """You find a big lake, but is  night and cold. 
        Where do you want to go? Type 'swim' or 'wait': """).lower().strip()

    if direction == "wait":
        print("Patience is a virtude, good choice!")

        direction = input(
            """Now you find a big room with 3 doors.
            Which door do you want to open?
            "Red", "Yellow", "Blue" or "Anything Else"? : """).lower().strip()

        if direction == "red":
            print("You are burned by fire. Game Over")
        elif direction == "yellow":
            print("You find the treasure. You Win!")
        elif direction == "blue":
            print("You are eaten by beasts. Game Over")
        else:
            print("You run, you are a coward. Game Over")
    else:
        print("You are attacked by Piranhas. Game Over!")
else:
    print("Fall into a hole. Game Over!")
