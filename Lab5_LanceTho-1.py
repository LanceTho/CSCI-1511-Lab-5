"""
Lab5_LanceTho-1.py
Lance Thongsavanh
Write a program that rolls two dice, prints the outcome, and then uses conditional statements to print the appropriate term for that roll based on the table below.
2/10/2026
"""

import random

#Challenge: Extend your program to include a while loop that continues to roll the dice and print the term until the user decides to quit.
user_input: str = ""
print("Roll dice? (y/n)")
user_input = input()

while(user_input == "y"):
    #Use the random module Print the value of each individual die and the total value of the roll.
    dice_roll1: int = random.randint(1,6)
    dice_roll2: int = random.randint(1,6)
    #Print the value of each individual die and the total value of the roll.
    print(f"First Dice Roll: {dice_roll1}")
    print(f"Second Dice Roll: {dice_roll2}")
    print(f"Total: {dice_roll1 + dice_roll2}")
    
    #checks if both dice values equals 1
    if(dice_roll1 == 1 and dice_roll2 == 1):
        #if true then prints the corresponding term
        print("Snake Eyes")

    #checks if one dice equals 1 and the other equal to 2 and vise versa
    if(dice_roll1 == 1 and dice_roll2 == 2):
        #if true then prints the corresponding term
        print("Ace Caught a Deuce")
    elif(dice_roll1 == 2 and dice_roll2 == 1):
        #if true then prints the corresponding term
        print("Ace Caught a Deuce")
    
    #checks if each dice values equals 2
    if(dice_roll1 == 2 and dice_roll2 == 2):
        #if true then prints the corresponding term
        print("Little Joe from Kokomo")

    #checks if one dice equals 1 and the other equal to 4 and vise versa
    if(dice_roll1 == 1 and dice_roll2 == 4):
        #if true then prints the corresponding term
        print("Little Phoebe")
    elif(dice_roll1 == 4 and dice_roll2 == 1):
        #if true then prints the corresponding term
        print("Little Phoebe")
    #checks if one dice equals 2 and the other equal to 3 and vise versa
    elif(dice_roll1 == 2 and dice_roll2 == 3):
        #if true then prints the corresponding term
        print("Little Phoebe")
    elif(dice_roll1 == 3 and dice_roll2 == 2):
        #if true then prints the corresponding term
        print("Little Phoebe")

    #checks if each dice values equals 3
    if(dice_roll1 == 3 and dice_roll2 == 3):
        #if true then prints the corresponding term
        print("Jimmy Hicks from the Sticks")

    #checks if one dice equals 6 and the other equal to 1 and vise versa
    if(dice_roll1 == 6 and dice_roll2 == 1):
        #if true then prints the corresponding term
        print("Six Ace")
    elif(dice_roll1 == 1 and dice_roll2 == 6):
        #if true then prints the corresponding term
        print("Six Ace")

    #checks if each dice values equals 4
    if(dice_roll1 == 4 and dice_roll2 == 4):
        #if true then prints the corresponding term
        print("Eighter from Deactur")

    #checks if one dice equals 3 and the other equal to 6 and vise versa
    if(dice_roll1 == 3 and dice_roll2 == 6):
        #if true then prints the corresponding term
        print("Nina from Pasadena")
    elif(dice_roll1 == 6 and dice_roll2 == 3):
        #if true then prints the corresponding term
        print("Nina from Pasadena")
    
    #checks if one dice equals 5 and the other equal to 4 and vise versa
    elif(dice_roll1 == 5 and dice_roll2 == 4):
        #if true then prints the corresponding term
        print("Nina from Pasadena")
    elif(dice_roll1 == 4 and dice_roll2 == 5):
        #if true then prints the corresponding term
        print("Nina from Pasadena")

    #checks if each dice values equals 5
    if(dice_roll1 == 5 and dice_roll2 == 5):
        #if true then prints the corresponding term
        print("Puppy Paws")

    #checks if one dice equals 5 and the other equal to 6 and vise versa
    if(dice_roll1 == 5 and dice_roll2 == 6):
        #if true then prints the corresponding term
        print("Six Five no Jive")
    elif((dice_roll1 == 6 and dice_roll2 == 5)):
        #if true then prints the corresponding term
        print("Six Five no Jive")

    #checks if each dice values equals 6
    if(dice_roll1 == 6 and dice_roll2 == 6):
        #if true then prints the corresponding term
        print("Boxcars")
    
    #prompt the user again and get user input
    print("Roll dice? (y/n)")
    user_input = input()