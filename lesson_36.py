from sys import exit

def left_restroom():
    print("Gabler Alex is here.")
    print("He is staring at you and won't let you exit ")
    print("How do you get rid of him? Scimitar, shrieking, or pleading?")
    gabler_moved= False

    while True:
        choice = input(">")
        if choice == "Scimitar" and not gabler_moved:
            print("You have defeated Gabler and exited the church")
            gabler_moved=True
        elif choice=="shrieking" and gabler_moved:
            dead("Gabler Alex eats you")
        elif choice=="pleading" and not gabler_moved:
            lobby()
        else:
             dead("You have been eaten by Gabler Alex")

def lobby():
    print("You have returned to the Christ Crossman lobby")
    print("You witness mass amounts of carnage ensuing")
    print("Do you run away or stay")
    while True:
        choice = input(">")
        if choice=="run away":
            print("Yay you're safe")
        else:
            dead("You die")

            
def dead(why):
    print(why, "Good job!")


def right_restroom():
    print("Stuart Michael Harrison is here")
    print("He has a jack hammer and is ready for complete destruction")
    print("How do you escape? Scytch, Mr. Jones by Counting Crows, or suffocation")
    stuart_moved= False
    while True:
        choice = input(">")
        if choice=="Sytch" and not stuart_moved:
            dead("Your weapon pales in comparison to Stuart's jackhmmer")
        elif choice=="Mr. Jones by Counting Crows" and not stuart_moved:
            westland_middle_school()
        else:
            dead("Stuart cannot be suffocated because he is not a human being")
def westland_middle_school():
    print("You and Stuart have teleported to Westland Middle School")
    print("You witness Mike Pickrel yielding a spork")
    print("He threatens to kill Stuart if you don't do 60 burpees")
    print("Do you do them?")
    burpees=False
    
    while True:
        choice = input(">")
        if choice == "no " and not burpees:
            dead("Stuart has passed")
        else:
            dead("You have passed")
        

def start():
    print("You are at Christ Crossman")
    print("They said use the bathrooms to the left and not the bathrooms to the right")
    print("Which bathroom will you use?")

    choice = input(">")

    if choice == "left":
        left_restroom()
    elif choice== "right":
        right_restroom()
    else:
        dead("You face the wrath of Chris Sabatini")

start()


