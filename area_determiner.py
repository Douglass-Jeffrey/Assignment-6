#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program calculates area using multiple functions


def triangle_calc(base, height):
    # This calculates area based on the base and height parameters
    # process
    area = (base * height) / 2
    return area


def main():
    while True:
        try:
            # Input
            base = int(input("Input the base of your triangle: "))
            height = int(input("Input the height of your triangle: "))

            # Calls area function
            area = triangle_calc(base, height)

            # output
            print("The area of your triangle is " + str(area)
                  + " units squared.")
            break
        except Exception:
            print("Please input only proper numbers, try again")


if __name__ == "__main__":
    main()
