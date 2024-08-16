# Data Types and Operators, Jackques Williams, v0.0

# Fundamental Data Types
# String - str - Sequence of letters, number, spaces, or other characteristics.
# String in Python are inside  ' ' or " "
#Idc if you use ' ' or " " just be consistent

# Boolean- bool- True or False values

# Float - float - any number value with a decimal including 0, +/-

# Integers - int - any whole number including 0, +/-

# Data Types are stored in VARIABLES.
# A Variable is basically a bucket with a name to put data into.
# VARIABLES NAME SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CAN'T START WITH A NUMBER
# camelCaseVariablesNames
# snake_case_variables_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 884654 # int data type
highScore = 294514 # int data types

carSpeed = 18.64 # float data type, miles per hour
car_speed = -9.5664848 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playerName = "Jackques Williams" # string data type
enemyType = "wind" # string data type

# Assign NEW VALUES
playerName = "Gambit"
carSpeed = "9.50"

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 4.5

# print Variables to Console / Screen
print(playerName)
print(isPurple)
print(highScore)
print(carSpeed)

# print variables and expression to console / screen
print(highScore + 9000)
print(45 * 2)
print(highScore)


# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello {playerName}. Your high score is {highScore}. \n")

# ARITHMETIC OPERATORS
myInt = 5
myFloat = 4.68
myNum = 0

# addition
myInt = 4 + 6
myFloat = 4.6 + 6.8

myInt = myInt + 5

myNum = myInt + myFloat 
# when you add an int  and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 32

# multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second is denominator

