#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 27, 2025
# This program calculates the leap or not leap year.


def main():
    # Gets the input year
    year = input("Enter the year.")
    # Catches any value errors such as if the input is a string and not integer.
    try:
        year = int(year)
        # First step of calculating of a leap year, where module answer supposed to be 0 otherwise it is not leap year, the same rule acts for other calculations, but in first one we just divide the year by 4.
        if year % 4 == 0:
            # If module was 0, we divide our year then by 100 with same rules acting above.
            if year % 100 == 0:
                # If module was 0, we divide our year by 400, same rules acting from first comment.
                if year % 400 == 0:
                    # Prints if it is a leap year if module is 0
                    print(f"The year {year} is a leap year.")
                # If module is not 0, then it prints that the year is not a leap year.
                else:
                    print(f"The year {year} is not a leap year.")
            # If module is not 0 upon division of 100 then it is a leap year.
            else:
                print(f"The year {year} is a leap year.")
        # If module is not 0 in our first division by 4, then it prints that year is not a leap year.
        else:
            print(f"The year {year} is not a leap year.")
            # Catches any errors.
    except Exception:
        print("Please enter a valid year")
        # Prints the goodbye statement upon finishing execution.
    finally:
        print("Thanks for using.")


if __name__ == "__main__":
    main()
