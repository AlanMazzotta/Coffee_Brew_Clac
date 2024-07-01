#******************************************************************************
# Author:         Alan Mazzotta
# Lab:            Lab 2
# Date:           7/1/2024
# Description:    This program calculates the boiling water to ground
#                 coffee ratio (17:1) for brewing a cup of pour over coffee in
#                 the user's desired coffee mug.
# Input:          Size of user's coffee mug in fluid ounces. Total amount of
#                 coffee desired by the user in fluid ounces.
# Output:         The amount of ground coffee required to brew the user's
#                 desired amount of coffee
# Sources:        Lab 2 instructions
# Notes:          Would like to add timer function in the future.
#                 Would like to limit 'How much coffee would you like (in
#                 fluid ounces)?' to 'How big is you coffee mug (in fluid
#                 ounces)?' or less to prevent overflow.
#                 Would also like to add a metric conversion but I think
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
#                 Would you like room for cream or non-dairy alternative (in
#                 fluid ounces, if no please enter 0)? __
#
#                 You will require __ oz of ground coffee,  __ oz of boiling
#                 water and of course your __ oz of cream or non-dairy
#                 alternative.
#******************************************************************************
# Welcome to the pour over brew calculator!
# How big is you coffee mug (in fluid ounces)? 12
# How much coffee would you like (in fluid ounces)? 10
#
# Calculating…
#
# You will require 0.59 oz (by volume) of ground coffee to brew 10 oz of coffee
# in your 12 oz mug.
# Enjoy your coffee!

floz_mug = 0.0
floz_desired= 0.0
coffee_oz_volume = 0.0

print("\nWelcome to the pour over brew calculator!")

floz_mug = float(input("\nHow big is you coffee mug (in fluid ounces)?: "))
floz_desired = float(input("How much coffee would you like (in fluid"
                           "ounces?: "))

print("\nCalculating...")

coffee_oz_volume = floz_desired/17

print("\nYou will require", format(coffee_oz_volume, "0.2f"), "oz (by volume) of ground"
" coffee" "\nto brew", format(floz_desired, "0.2f"), "oz of coffee in your"
, format(floz_mug, "0.2f"), "oz mug.")