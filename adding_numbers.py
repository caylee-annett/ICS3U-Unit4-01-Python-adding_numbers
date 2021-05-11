#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program adds integers from 1 to the user's input and uses loops


def main():
    # This function adds the numbers
    loop_counter = 0

    # Input
    print("This program adds numbers from 1 to what you enter.")
    number_as_string = input("Enter a positive integer: ")
    print("")

    # Process & Output
    try:
        number_as_integer = int(number_as_string)

        while loop_counter < (number_as_integer / 2) * (1 + number_as_integer):
            loop_counter = loop_counter + 1
        print("The sum of all the integers from 1 to {0} is {1}."
              .format(number_as_integer, loop_counter))
    except Exception:
        print("{} is not a valid input.".format(number_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
