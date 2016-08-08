#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_input = ''
    while user_input == '':
        try:
            user_input = int(input("Type an integer: "))
        except:
            print("you didn't input a number")
    if user_input % 2 == 0:
        print("{} is an even number".format(user_input))
    else:
        print("{} is an odd number".format(user_input))
      


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for number in range(1, 101):
        if number % 10 == 0:
            print("{:<3} \n".format(number))
        else:
            print("{:<3}".format(number), end=" ") 


    


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = input("Please type a number: ") 
    count = 0
    total = 0
    average = None
    while user_input != 'done':
        try:
            user_input = float(user_input)
            total += float(user_input)
            count += 1 
            average = total / count
        except:
            print("That is not a number.")
        user_input = input("Please type a number: ")    
    return average




##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())

if __name__ == '__main__':
    main()
