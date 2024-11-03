"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"
# Charge for this sign.
charge = 35.00
# Number of characters.
numChars = int(input("Please enter the number of characters your sign will include: "))
# Color of characters.
color = input("Please enter the color you would like the characters on your sign to be (white, black, or gold): ")
# Type of wood.
woodType = input("Please enter desired wood type for your sign (oak or pine): ")
# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge = charge + (4 * (numChars - 5))
    
if woodType == "oak":
    charge = charge + 20.00
    
if color == "gold":
    charge = charge + 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
