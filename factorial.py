#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program calculates the factorial


def main():
    # this function uses a loop

    # this is to keep track of the loop and calculate the sum
    loop_counter = 1
    total = 1

    # input
    user_input_string = input("Enter a positive integer : ")

    # process & output
    try:
        user_input = int(user_input_string)
        if user_input >= 0:
            while loop_counter <= user_input:
                total = total * loop_counter
                loop_counter = loop_counter + 1
            else:
                print("{0}! = {1}".format(user_input, total))
        else:
            print("Negative integer entered. Please try again.")
    except Exception:
        print("Invalid input.")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
