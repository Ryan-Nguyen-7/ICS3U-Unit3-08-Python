# Created by Ryan Nguyen
# Created on December 2020
# This program checks if a year is a leap year

import constants

def main():
    # This function checks if a year is a leap year

    # input
    year_as_string = input("Enter year: ")
    print("")

    # process + output
    try:
        year_as_number = int(year_as_string)
        if year_as_number % constants.RULES_A == 0:
            if year_as_number % constants.RULES_B == 0:
                if year_as_number % constants.RULES_C == 0:
                    print("Leap year")
                else:
                    print("Not a leap year")
            else:
                print("Leap year")
        else:
            print("Not a leap year")
    except Exception:
        print("Not a year")


if __name__ == "__main__":
    main()
