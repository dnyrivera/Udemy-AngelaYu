# 1 - Write a program in main.py that prints some notes on Python programming into the Output console.
print('what to print')


# 2 - Look at the code in the code editor on the left. There are errors in all of the lines of code. Fix the code so that it runs without errors.
# String Concatenation is done with the "+" sign.
# New lines can be created with a backslash and n.

# 1. Missing double quotes before the word Day.
print("Day 1 - String Manipulation")
# 2. Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+" sign.')
# 3. Extra indentation removed
print('e.g. print("Hello " + "world")')


# 3 - Write a program that prints the number of characters in a name.
# NOTE: You can access the value in the input pane using the input() function.
# IMPORTANT: Don't add anything inside the input() function. e.g. use name = input() rather than: name = input("What's your name?")
# Example Input : Jane
# Example Output: 4
print(len(input()))


# 4 - This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.
# Write a program that switches the values stored in the variables a and b.
# Warning . You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.

# Example Input 1 : 29 / 41
# Example Output 1 : a: 41 / b: 29

# There are two variables, a and b
a = input()
b = input()
# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

