# Flow Control Structures, Jackques Williams, v0.0
# Making Computer Programs Make Decisions

temperature = 188.29
color = "Black"
height = 8
likesPineappleOnPizza = True 

# SINGLE DECISION POINT - if statement
# if CONDITIONAL_EXPESSION: <-- This will use a COMPARISON OPERATOR 99% of the time
#       runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
   print("It is hot as the sun outside.\n")

if height < 10:
    print("you not good.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza: 
    print("Nasty")

# What if we want something different to happen
if color == "Black" : # COMMON ERROR FOR STUDENTS IS USING instead of ==.
    print("Your shirt is the correct  unitform color\n")
else:
     print("Your shirt is not the correct  unitform color\n")

if temperature == 188.92:
    print("It is hot as heck")
else:
    print("It is too cold")
