# *****************************************************************************
# Author:       	Ari P.
# Assignment:       Assignment 3
# Date:         	2/12/2025
# Description:  	This program will sort and display a list of D&D monsters
#                   and their challenge ratings entered by the user.
# Input:        	Monster names (string), monster CRs (float)
# Output:       	Welcome message (string), monster names (string), monster
#                   CRs (float), monster table (string), goodbye message
#                   (string)
# Sources:      	Assignment 3 specifications, assignment 3 sample, python
#                   style guide, W3Schools python reference
# *****************************************************************************

def main():
    # Create paired lists for monster names and CRs
    monsterNames = []
    monsterRatings = []
    # Create variables for inputs
    nameInput = ""
    ratingInput = ""
    # Create variables for loops
    finished = False
    valid = False
    correct = False
    length = 0
    largest = 0.0
    largestIndex = 0
    # Create variable for table formatting
    justify = 0

    # Print welcome message
    print("Enter a list of D&D monster names and their associated challenge ra"
    "tings (CR). This program will sort them into a table from highest to lowe"
    "st CR.")

    # Prompt for input
    print("\nBegin entering monsters (leave blank when finished). CR can also "
    "be 0, 1/8, 1/4, or 1/2.")
    # Loop until they enter nothing
    while not finished:
        valid = False
        correct = False
        # Get name
        nameInput = " ".join(str(input("\nName: ")).split())
        if nameInput == "":
            finished = True
        else:
            # Loop for input validation
            while not valid or not correct:
                # Get CR
                ratingInput = "".join(str(input("CR: ")).split())
                if ratingInput == "":
                    valid = True
                    correct = True
                elif ratingInput == "1/8":
                    valid = True
                    correct = True
                elif ratingInput == "1/4":
                    valid = True
                    correct = True
                elif ratingInput == "1/2":
                    valid = True
                    correct = True
                else:
                    try:
                        ratingInput = float(ratingInput)
                        valid = True
                    except:
                        print("Invalid CR!")
                    if valid == True:
                        if ratingInput == 0.0:
                            correct = True
                        elif ratingInput == .125:
                            correct = True
                        elif ratingInput == .25:
                            correct = True
                        elif ratingInput == .5:
                            correct = True
                        elif ratingInput >= 1.0:
                            correct = True
                        else:
                            print("Invalid CR!")
            if ratingInput == "":
                finished = True
            else:
                # Add name and CR to lists
                monsterNames.append(nameInput)
                if ratingInput == "1/8":
                    monsterRatings.append(.125)
                elif ratingInput == "1/4":
                    monsterRatings.append(.25)
                elif ratingInput == "1/2":
                    monsterRatings.append(.5)
                else:
                    monsterRatings.append(float(ratingInput))

    # Get number of entries
    length = len(monsterNames)
    if length < 1:
        print("You didn't enter any monsters...")
    else:
        # Find longest entry
        justify = len(monsterNames[0])
        for count in range(0, length):
            if len(monsterNames[count]) > justify:
                justify = len(monsterNames[count])
        
        print("Generating table...\n")
        print("Monster".ljust(justify + 4), "CR", sep = "")
        # Loop through each entry
        for i in range(0, length):
            largest = monsterRatings[0]
            largestIndex = 0
            # Find largest CR
            for count in range(0, len(monsterRatings)):
                if monsterRatings[count] > largest:
                    largest = monsterRatings[count]
                    largestIndex = count
            # Print name
            print(monsterNames[largestIndex].ljust(justify + 4), end = "")
            # Print CR
            if monsterRatings[largestIndex] == .125:
                print("1/8")
            elif monsterRatings[largestIndex] == .25:
                print("1/4")
            elif monsterRatings[largestIndex] == .5:
                print("1/2")
            else:
                print(str(int(monsterRatings[largestIndex])))
            # Remove current monster from lists
            del monsterNames[largestIndex]
            del monsterRatings[largestIndex]
    
    # Print goodbye message
    print("\nCome back after you've bought the new monster manual!")

main()