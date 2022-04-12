#!/usr/bin/env python3

# Created by: Sarah
# Created on: April 12, 2022
# This program determines if the year entered is a 
# leap year or not. 


def main():
    user_year_string = input("Enter a year (ex. 2006): ")
    print("")
    try:
        # changing string into an integer
        user_year_int = int(user_year_string)

        # sets a range
        if user_year_int < 1:
            print("Please enter a positive number.")
        else:

            # checks to see if the year entered is leap year or not.
            if (user_year_int % 4) == 0:
                if (user_year_int % 100) == 0:
                    if (user_year_int % 400) == 0:
                        # displays that it is a leap year
                        print("This is a leap year!")
                        print("It has 366 days.")
                    else:
                        print("This is not a leap year.")
                else:
                    print("This is a leap year.")
                    print("It has 366 days.")
            else:
                print("This is not a leap year.")

        # checks for errors
    except Exception:
        print("{} is not a valid year.". format(user_year_string))


if __name__ == "__main__":
    main()
