# ******************************************************************************
# Author:         Alan Mazzotta
# Lab:            Lab 4
# Date:           7/23/2024
# Description:    This program calculates the boiling water to ground
#                 coffee ratio (17:1) for brewing a cup of pour over coffee in
#                 the user's desired coffee mug.
# Input:          Size of user's coffee mug in fluid ounces. Total amount of
#                 coffee desired by the user in fluid ounces.
# Output:         The amount of ground coffee required to brew the user's
#                 desired amount of coffee
# Sources:        Lab 4 instructions
# Notes:          Would like to add timer function in the future.
#                 Would like to limit 'How much coffee would you like (in
#                 fluid ounces)?' to 'How big is you coffee mug (in fluid
#                 ounces)?' or less to prevent overflow.
#                 Would also like to add a metric conversion, but I think
#                 I'll wait for the if/then statements I assume are coming up.
#                 Sample
#                 Would you like your measurements in grams? Metric tends to
#                 be more accurate at average coffee mug volumes. __yes/no
#
#                 You will require __ g of ground coffee and __ g of boiling
#                 water.
#
#                 Would also like to add a scenario for "Room for cream?"
#                 Sample
#                 How big is you coffee mug (in fluid ounces)? __
#                 Would you like room for cream or non-dairy alternative? (y/n) __
#                 How much cream or non-dairy alternative (in fluid ounces)? __
#
#                 You will require __ oz of ground coffee,  __ oz of boiling
#                 water and of course your __ oz of cream or non-dairy
#                 alternative.
# ******************************************************************************
# Sample Run
#
# Welcome to the pour over brew calculator!
#
# How big is you coffee mug (in fluid ounces)? 12
# How much coffee would you like (in fluid ounces)? 10
# Would you like room from cream or non-dairy alternative? (y/n) y
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
# Sample Run 1.0
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
#
# You will require 0.59 oz (by volume) of ground coffee and 1 oz cream
# to brew 10 oz of coffee in your 12 oz mug.
#
# Enjoy your coffee!

def main():  # main function
    floz_mug = 0.0
    floz_desired = 0.0
    roomForCream = bool(float)
    floz_cream = 0.0
    coffee_oz_volume = 0.0

    print_welcome()  # welcome call

    # Inputs
    floz_mug = get_floz_mug()  # input mug volume call
    floz_desired = get_floz_desired()  # input coffee volume desired call
    want_roomForCream()  # input if cream is desired call
    floz_cream = get_floz_cream(roomForCream)  # input cream volume desired call

    print_calculating()  # computer is calculating call

    # Calculations
    coffee_oz_volume = calc_coffee_oz(floz_desired)  # brew calculation call

    # Outputs
    get_overflow(floz_desired, floz_mug, floz_cream)  # output determines if the coffee will
    # overflow or not call
    print_final_brew_oz(coffee_oz_volume, floz_desired, floz_mug, floz_cream)
    # output of brew calculator

    print_enjoy()  # enjoy call


# ******************************************************************************


def print_welcome():
    """
    Print welcome message
    """
    print("\nWelcome to the pour over brew calculator!")


def get_floz_mug():
    """
    Asks the user to enter coffee mug volume (in fluid ounces)
    :return: floz_mug: float
    """
    floz_mug = 0.0
    floz_mug = float(input("\nHow big is you coffee mug (in fluid ounces)?: "))
    return floz_mug


def get_floz_desired():
    """
    Asks the user to enter coffee desired (in fluid ounces)
    :return: floz_desired: float
    """
    floz_desired = 0.0
    floz_desired = float(input("How much coffee would you like (in fluid"
                               "ounces?: "))
    return floz_desired


def get_overflow(floz_desired, floz_mug, floz_cream):
    """
    determines if the coffee will overflow or not
    param floz_desired: float
    param floz_mug: float
    """
    if floz_desired + floz_cream > floz_mug:
        print("\nDo not overfill you mug! Nobody likes a mess.")
    else:
        print("\nEverything looks good.")


def want_roomForCream():
    """
    Asks the user to enter room for cream
    :return: room_for_cream: string
    """
    roomForCream = bool(float)
    roomForCream = input("Would you like room from cream or non-dairy alternative? (y/n): ")
    if roomForCream == "y":
        return 1
    else:
        return 0


def get_floz_cream(roomForCream):
    """
    Asks the user to enter the amount of cream desired (in fluid ounces)
    param roomForCream: string
    :return: howMuchCream: float or 0.0
    """
    floz_cream = 0.0
    if roomForCream == 1:
        floz_cream = float(input("How much cream or non-dairy alternative (in fluid ounces)?: "))
        return floz_cream
    else:
        return 0


def print_calculating():
    """
    message the computer is calculating.
    """
    print("\nCalculating...")


def calc_coffee_oz(floz_desired):
    """
    Calculate the boiling water (in fluid ounces) to brew coffee.
    :param floz_desired: float, the desired coffee volume
    :return: float, the boiling water volume in fluid ounces
    """
    return floz_desired / 17


def print_final_brew_oz(coffee_oz_volume, floz_desired, floz_mug, floz_cream):
    """
    Print the final brew ratio in ounces.
    """
    print("\nYou will require", format(coffee_oz_volume, "0.2f"),
          " oz (by volume) of ground coffee and", format(floz_cream, "0.2f"),
          "oz cream"
          "\nto brew", format(floz_desired, "0.2f"),
          "oz of coffee in your", format(floz_mug, "0.2f"), "oz mug.")


def print_enjoy():
    """
    Print the enjoy your coffee message
    """
    print("\nEnjoy your coffee!")


main()
