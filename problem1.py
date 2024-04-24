#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""

length_box = float(input("enter box length: "))

if float(int(length_box))==length_box:
    length_box = int(length_box)

    for h in range(0, length_box):
        print("")
        for w in range(0, length_box):

            print("* ", end="")
else:
    print("error; not a interger")