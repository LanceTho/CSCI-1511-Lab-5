"""
Lab5_LanceTho-1.py
Lance Thongsavanh
Write a program that rolls two dice, prints the outcome, and then uses conditional statements to print the appropriate term for that roll based on the table below.
2/9.2026
"""

import random

#Challenge: Extend your program to include a while loop that continues to roll the dice and print the term until the user decides to quit.

#Use the random module Print the value of each individual die and the total value of the roll.
dice_roll1: int = random.randint(1,6)
dice_roll2: int = random.randint(1,6)

#Print the value of each individual die and the total value of the roll.
print(f"First Dice Roll: {dice_roll1}")
print(f"Second Dice Roll: {dice_roll2}")
print(f"Total: {dice_roll1 + dice_roll2}")
#Use if->elif->else conditional statements to check the roll and print the correct term, you may also need to use complex conditionals using 'AND', 'OR', and 'not'  for every variabtion in the role to match the correct terms
#Pay close attention to the table.  Some terms are vased on the total, while others are based on specific die values (e.g., "Little Joe").
"""
Use this table:
1, 1            -> 2 -> Snake Eyes
1, 2 or 2, 1    -> 3 -> Ace Caught a Deuce
2, 2            -> 4 -> Little Joe from Kokomo
1, 4 or 4, 1    -> 5 -> Little Phoebe
2, 3 or 3, 2    -> 5 -> Little Phoebe
3, 3            -> 6 -> Jimmy Hicks from the Sticks
6, 1 or 1, 6    -> 7 -> Six Ace 
4, 4            -> 8 -> Eighter from Deactur
3, 6 or 6, 3    -> 9 -> Nina from Pasadena
4, 5 or 5, 4    -> 9 -> Nina from Pasadena
5, 5            -> 10 -> Puppy Paws
6, 5 or 5, 6    -> 11 -> Six Five no Jive
6, 6            -> 12 -> Boxcars
"""
if(dice_roll1 == 1 and dice_roll2 == 1):
    print("Snake Eyes")

if(dice_roll1 == 1 and dice_roll2 == 2):
    print("Ace Caught a Deuce")
elif(dice_roll1 == 2 and dice_roll2 == 1):
    print("Ace Caught a Deuce")

if(dice_roll1 == 2 and dice_roll2 == 2):
    print("Little Joe from Kokomo")

if(dice_roll1 == 1 and dice_roll2 == 4):
    print("Little Phoebe")
elif(dice_roll1 == 4 and dice_roll2 == 1):
    print("Little Phoebe")
elif(dice_roll1 == 2 and dice_roll2 == 3):
    print("Little Phoebe")
elif(dice_roll1 == 3 and dice_roll2 == 2):
    print("Little Phoebe")

if(dice_roll1 == 3 and dice_roll2 == 3):
    print("Jimmy Hicks from the Sticks")

if(dice_roll1 == 6 and dice_roll2 == 1):
    print("Six Ace")
elif(dice_roll1 == 1 and dice_roll2 == 6):
    print("Six Ace")

if(dice_roll1 == 4 and dice_roll2 == 4):
    print("Eighter from Deactur")

if(dice_roll1 == 3 and dice_roll2 == 6):
    print("Nina from Pasadena")
elif(dice_roll1 == 6 and dice_roll2 == 3):
    print("Nina from Pasadena")
elif(dice_roll1 == 5 and dice_roll2 == 4):
    print("Nina from Pasadena")
elif(dice_roll1 == 4 and dice_roll2 == 5):
    print("Nina from Pasadena")

if(dice_roll1 == 5 and dice_roll2 == 5):
    print("Puppy Paws")

if(dice_roll1 == 5 and dice_roll2 == 6):
    print("Six Five no Jive")
elif((dice_roll1 == 6 and dice_roll2 == 5)):
    print("Six Five no Jive")

if(dice_roll1 == 6 and dice_roll2 == 6):
    print("Boxcars")