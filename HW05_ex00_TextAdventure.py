#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

user_name = input('Your name: ')

def back_room():
    print("{} discovers a back room".format(user_name))
    print("It's filled with awesome programmers.")
    print('{} says, "Hello, everyone. my name is {}."'.format(user_name, user_name))
    print("Everyone welcomes {} and asks {} to start programming".format(user_name, user_name))
    print("{} starts programming Python and never leave.".format(user_name))
    exit(0)




def infinite_stairway_room(count=0):
    print("{} walk through the door to see a dimly lit hallway.".format(user_name))
    print("At the end of the hallway is a {}staircase going towards some light".format(count * 'long '))
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('{} takes the stairs'.format(user_name))
        if (count > 0):
            print("but {} is not happy about it".format(user_name))
        infinite_stairway_room(count + 1)
    # option 2 == discover the back room
    else:
        back_room()
        


def gold_room():
    print("This room is full of gold.  How much do {} take?".format(user_name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {}'s not greedy, {} win!".format(user_name, user_name))
        exit(0)
    else:
        dead("{} greedy goose!".format(user_name))


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(user_name))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at {} then slaps your face off.".format(user_name))
        elif next == "taunt bear" or next == "taunt" and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(user_name))
            bear_moved = True
        elif next == "taunt bear" or next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" or next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here {} see the great evil Cthulhu.".format(user_name))
    print("He, it, whatever stares at {} and {} go insane.".format(user_name, user_name))
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room(count=0)
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("{} is in a dark room.".format(user_name))
    print("There is a door to your right and left.")
    print("Which one does {} take?".format(user_name))

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("{} stumble around the room until {} starve.".format(user_name, user_name))

if __name__ == '__main__':
    main()
