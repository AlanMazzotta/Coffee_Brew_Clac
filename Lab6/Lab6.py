# ******************************************************************************
# Author:         Alan Mazzotta
# Lab:            Lab 6
# Date:           8/21/2024
# Description:    This program calculates the boiling water to ground
#                 coffee ratio (17:1) for brewing a cup of pour over coffee in
#                 the user's desired coffee mug.
# Input:          Size of user's coffee mug in fluid ounces (validated). Total amount of
#                 coffee desired by the user in fluid ounces (validated).
# Output:         The amount of ground coffee required to brew the user's
#                 desired amount of coffee
# Sources:        Lab 6 instructions
# Pseudocode      1. Welcome user.
#                 2. Ask how big the mug is (fl oz).
#                 3. Ask the user how much coffee they want (fl oz).
#                 4. Ask the user if they want cream.
#                 5. Ask the user how much cream (fl oz).
#                 6. Calculate if the user's mug is too small for
#                    that amount of coffee and cream.
#                    If mug is appropriately sized calculate and provide result
#                    Determine if the mug is too small ask user to try again.
#                    Determine if negative values were input
#                    and ask the user to try again.
# ******************************************************************************
# Sample Run 1.0
#
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 12
# How much coffee would you like (in fluid ounces)? 10
# Would you like room from cream or non-dairy alternative? (y/n): y
# How much cream or non-dairy alternative (in fluid ounces)?: 1
#
# Calculating…
#
# Everything looks good.
#
# You will require 0.59 oz (by volume) of ground coffee and 1 oz cream
# to brew 10 oz of coffee in your 12 oz mug.
#
# Enjoy your coffee!
#
# Sample Run 1.1
#
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 8
# How much coffee would you like (in fluid ounces)? 12
# Would you like room from cream or non-dairy alternative? (y/n) n
#
# Calculating…
#
# Do not overfill you mug! Nobody likes a mess.
# Would you like to try again with a bigger mug or less coffee
# or cream? (y/n) y
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 12
# How much coffee would you like (in fluid ounces)? 10
# Would you like room from cream or non-dairy alternative? (y/n): n
#
# Calculating…
#
# You will require 0.59 oz (by volume) of ground coffee and 0 oz cream
# to brew 10 oz of coffee in your 12 oz mug.
#
# Enjoy your coffee!
#
# Sample Run 1.2
#
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? -1
# How much coffee would you like (in fluid ounces)? -6
# Would you like room from cream or non-dairy alternative? (y/n) n
#
# Calculating…
#
# A negative value indicates you may not actually want any coffee.
# Would you like to try again with a bigger mug or less coffee or cream?
#  (y/n): y
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 12
# How much coffee would you like (in fluid ounces)? 10
# Would you like room from cream or non-dairy alternative? (y/n): n
#
# Calculating…
#
# You will require 0.59 oz (by volume) of ground coffee and 0 oz cream
# to brew 10 oz of coffee in your 12 oz mug.
#
# Enjoy your coffee!
#
# Sample Run 1.3
#
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 12
# How much coffee would you like (in fluid ounces)? 10
# Would you like room from cream or non-dairy alternative? (y/n): y
# How much cream or non-dairy alternative (in fluid ounces)?: 3
#
# Calculating…
#
# Do not overfill you mug! Nobody likes a mess.
# Would you like to try again with a bigger mug or less coffee or cream? (y/n): y
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 16
# How much coffee would you like (in fluid ounces)? 10
# Would you like room from cream or non-dairy alternative? (y/n): y
# How much cream or non-dairy alternative (in fluid ounces)?: 3
#
# Calculating…
#
# You will require 0.59 oz (by volume) of ground coffee and 3 oz cream
# to brew 10 oz of coffee in your 16 oz mug.
#
# Enjoy your coffee!

import valid as v

def main():
    floz_mug = 0.0
    floz_desired = 0.0
    floz_cream = 0.0
    room_for_cream = True
    try_again = False
    overflow = True

    while try_again == False:
        print_welcome()  # welcome call
        floz_mug = get_floz_mug()  # input mug volume call
        floz_desired = get_floz_desired()  # input coffee volume desired call
        room_for_cream = want_room_for_cream()  # input if cream is desired call
        floz_cream = get_floz_cream(room_for_cream)  # input cream volume desired call
        print_calculating()  # computer is calculating call
        overflow = get_overflow(floz_desired, floz_mug, floz_cream)  # output
        # determines if the coffee will overflow or not or if negative value was input call
        # if there is overflow  do not coffee oz volume, print final brew oz, print enjoy
        coffee_oz_volume = calc_coffee_oz(floz_desired)  # brew calculation call
        print_final_brew_oz(coffee_oz_volume, floz_desired, floz_mug, floz_cream, overflow)  # output
        # of brew calculator
        print_enjoy(overflow)  # Enjoy call
        try_again = get_try_again(try_again)  # input if user would like to try again call


def get_overflow(floz_desired, floz_mug, floz_cream):
    """
    determines if the coffee will overflow or not
    :param: floz_desired: (float) amount of coffee the user entered
    :param: floz_mug: (float) size of user's coffee mug
    :param: floz_cream: (float) amount of cream the user entered
    :return: (bool) True if the coffee will not overflow,
     False if coffee will overflow or negative value entered
    """
    if floz_desired + floz_cream < 0:
        print("\nA negative value indicates you may not actually want any coffee.")
        return False
    elif floz_desired + floz_cream > floz_mug:
        print("\nDo not overfill you mug! Nobody likes a mess.")
        return False
    else:
        print("\nEverything looks good.")
        return True


def print_welcome():
    """
    Print welcome message
    """
    print("\nWelcome to the pour over brew calculator!")


def get_floz_mug():
    """
    Asks the user to enter coffee mug volume (in fluid ounces) and validates the input
    :return: floz_mug: (float) size of user's coffee mug : validated
    """
    floz_mug = 0.0
    floz_mug = v.get_real("\nHow big is your coffee mug (in fluid ounces)?: ")
    while floz_mug <= 0:
        print("\nPlease enter a real number greater than 0.")
        floz_mug = v.get_real("\nHow big is your coffee mug (in fluid ounces)?: ")
    return floz_mug


def get_floz_desired():
    """
    Asks the user to enter coffee desired (in fluid ounces) and validates the input
    :return: floz_desired: (float) amount of coffee the user entered : validated
    """
    floz_desired = 0.0
    floz_desired = v.get_real("How much coffee would you like (in fluid"
                               " ounces)?: ")
    while floz_desired <= 0:
        print("\nPlease enter a real number greater than 0.")
        floz_desired = v.get_real("How much coffee would you like (in fluid"
                                  " ounces)?: ")
    return floz_desired


def want_room_for_cream():
    """
    Asks the user to enter room for cream and validates the input
    :return: room_for_cream: (bool) True or False if the user wants
     to enter room for cream : validated
    """
    room_for_cream = True
    room_for_cream = v.get_y_or_n("Would you like room from"
                           " cream or non-dairy alternative? (y/n): ")
    if room_for_cream == "y":
        return 1
    else:
        return 0


def get_floz_cream(room_for_cream):
    """
    Asks the user to enter the amount of cream desired (in fluid ounces) and validates the input
    param roomForCream: (bool) True or False
    :return: (float) or 0.0 amount of cream the user entered : validated
    """
    floz_cream = 0.0
    if room_for_cream == 1:
        floz_cream = v.get_real("How much cream or non-dairy"
                                 " alternative (in fluid ounces)?: ")
        while floz_cream <= 0:
            print("\nPlease enter a real number greater than 0.")
            floz_cream = v.get_real("How much cream or non-dairy"
                                    " alternative (in fluid ounces)?: ")
        return floz_cream
    else:
        return 0


def print_calculating():
    """
    message the computer is calculating.
    """
    print("\nCalculating...")


def get_try_again(try_again):
    """
    Asks the user to enter try again and validates the input.
    :param try_again: (bool) True or False
    :return: try_again: (bool) True or False : validated
    """
    try_again = 'y'
    try_again = v.get_y_or_n("Would you like to try again with a bigger"
                      " mug or less coffee or cream? Or do you"
                      " just need another cup? (y/n): ")
    if try_again == 'y':
        return False
    else:
        return True


def calc_coffee_oz(floz_desired):
    """
    Calculate the boiling water (in fluid ounces) to brew coffee.
    :param floz_desired: (float) the desired coffee volume
    :return: fl_oz desired: (float) the boiling water volume in fluid ounces:
    """
    return floz_desired / 17


def print_final_brew_oz(coffee_oz_volume, floz_desired, floz_mug, floz_cream, overflow):
    """
    Print the final brew ratio in ounces.
    :param: coffee_oz_volume: (float) the boiling water volume in fluid ounces
    :param: floz_desired: (float) amount of coffee the user entered
    :param: floz_mug: (float) size of user's coffee mug
    :param: floz_cream: (float) amount of cream the user entered
    :param: overflow: (bool) True if the coffee will not overflow,
     False if coffee will overflow or negative value entered
    """
    if overflow == True:
        print("\nYou will require", format(coffee_oz_volume, "0.2f"),
              " oz (by volume) of ground coffee and", format(floz_cream, "0.1f"), "oz cream"
                                                                                  "\nto brew",
              format(floz_desired, "0.1f"),
              "oz of coffee in your", format(floz_mug, "0.1f"), "oz mug.")


def print_enjoy(overflow):
    """
    Print the enjoy your coffee message
    :param: overflow (bool) True if the coffee will not overflow,
     False if coffee will overflow or negative value entered
    """
    if overflow == True:
        print("\nEnjoy your coffee!")


main()
