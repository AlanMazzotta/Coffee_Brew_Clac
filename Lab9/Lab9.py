# ******************************************************************************
# Author:         Alan Mazzotta
# Lab:            Lab 9
# Date:           8/30/2024
# Description:    This program calculates the boiling water to ground
#                 coffee ratio (17:1) for brewing a cup of pour over coffee in
#                 the user's desired coffee mug.
# Input:          Size of user's coffee mug in fluid ounces (validated). Total amount of
#                 coffee desired by the user in fluid ounces (validated).
# Output:         The amount of ground coffee required to brew the user's
#                 desired amount of coffee
# Sources:        Lab 9 instructions
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


class Brew:
    __floz_mug = 0.0
    __floz_desired = 0.0
    __floz_cream = 0.0
    __coffee_oz_volume = 0.0

    def __init__(self, mug, desired, cream, coffee):
        self.__floz_mug = mug
        self.__floz_desired = desired
        self.__floz_cream = cream
        self.__coffee_oz_volume = coffee

    def __str__(self):
        return " {:<8.1f}  {:<32.2f}  {:<15.1f}  {:<23.2f}".format(self.__floz_mug,
                                                                   self.__floz_desired,
                                                                   self.__floz_cream,
                                                                   self.__coffee_oz_volume)

    def get_floz_mug(self):
        return self.__floz_mug

    def get_floz_desired(self):
        return self.__floz_desired

    def get_floz_cream(self):
        return self.__floz_cream

    def get_coffee_oz_volume(self):
        return self.__coffee_oz_volume

    def set_floz_mug(self, mug):
        self.__floz_mug = mug

    def set_floz_desired(self, desired):
        self.__floz_desired = desired

    def set_floz_cream(self, cream):
        self.__floz_cream = cream

    def set_coffee_oz_volume(self, coffee):
        self.__coffee_oz_volume = coffee


def main():
    floz_mug = 0.0
    floz_desired = 0.0
    floz_cream = 0.0
    coffee_oz_volume = 0.0
    room_for_cream = True
    try_again = False
    overflow = True
    brew_list = []

    while try_again == False:
        print_welcome()  # welcome call
        floz_mug = get_floz_mug()  # input mug volume call
        floz_desired = get_floz_desired()  # input coffee volume desired call
        room_for_cream = want_room_for_cream()  # input if cream is desired call
        floz_cream = get_floz_cream(room_for_cream)  # input cream volume desired call
        print_calculating()  # computer is calculating call
        brew_list.append(Brew(floz_mug, floz_desired, floz_cream, coffee_oz_volume))  # add this cup to history
        coffee_oz_volume = calc_coffee_oz(brew_list)  # brew calculation call
        brew_list[-1].set_coffee_oz_volume(coffee_oz_volume)  # record this cup's calculated coffee amount
        overflow = get_overflow(brew_list)  # output
        # determines if the coffee will overflow or not or if negative value was input call
        # if there is overflow  do not coffee oz volume, print final brew oz, print enjoy
        print_final_brew_oz(brew_list, overflow)  # output
        # of brew calculator
        try_again = get_try_again(try_again)  # input if user would like to try again call
    print_brew_history(brew_list)


def print_brew_history(brew_list):
    """
    Returns a list of the brew history
    """
    print("\nYour brew history was...")
    print(" {:<8}  {:<32}  {:<15}  {:<23}".format("Mug size", "Amount of boiling water required",
                                                  "Amount of cream", "Amount of ground coffee"))
    for brew in brew_list:
        print(brew)


def get_overflow(brew_list):
    """
    determines if the most recently added cup will overflow or not
    :param: brew_list : (list) size of user's brew requirements
    :return: (bool) True if the coffee will not overflow,
     False if coffee will overflow or negative value entered
    """
    latest = brew_list[-1]
    if latest.get_floz_desired() + latest.get_floz_cream() > latest.get_floz_mug():
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


def calc_coffee_oz(brew_list):
    """
    Calculate the boiling water (in fluid ounces) to brew coffee.
    :param brew_list: (list) the brew history list
    :return: coffee_oz_volume : (float) the boiling water volume in fluid ounces:
    """
    coffee_oz_volume = 0.0
    for i in range(len(brew_list)):
        coffee_oz_volume = (brew_list[i].get_floz_desired() / 17)
    return coffee_oz_volume


def print_final_brew_oz(brew_list, overflow):
    """
    Print a one-line summary for the cup just brewed, followed by the full
    brew history table (including this cup).
    :param: brew_list : (list) the boiling water volume in fluid ounces list
    :param: overflow: (bool) True if the coffee will not overflow,
     False if coffee will overflow or negative value entered
    """
    if overflow == True:
        latest = brew_list[-1]
        print("\nYou will require", format(latest.get_floz_desired(), "0.1f"),
              "oz of boiling water and", format(latest.get_coffee_oz_volume(), "0.2f"),
              "oz (by weight) of ground coffee,"
              "\nplus", format(latest.get_floz_cream(), "0.1f"), "oz cream,",
              "for your", format(latest.get_floz_mug(), "0.1f"), "oz mug.")
        print("\nEnjoy your coffee!")
        print_brew_history(brew_list)


main()
