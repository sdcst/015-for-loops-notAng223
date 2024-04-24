#!python3

"""
##### Problem 2
Calculate the factorial of a number. 

 4! does not mean 4 is excited, it's the notation for a factorial.
A factorial is a special operation in math that is used in probability 
and combination problems.  For example, if you have 4 people, the number
of ways that they can be lined up against the wall is 4!

A factorial is defined as:
5! = 1 * 2 * 3 * 4 * 5
5! = 120

3! = 1 * 2 * 3
3! = 6

Note that a factorial can only accept an integer as an input number.  
Your program should also include some "input validation". This means that
the program will only determine the factorial IF the input is a positive
integer.  If the number is not a positive integer, it will display 
"Invalid input"

inputs:
int number

outputs:
"xx! is yy" where xx is the integer entered and yy is the calculated answer
Invalid input

example:
Enter a number: 4
4! is 24

example:
Enter a number: -4
Invalid input
"""


from typing_extensions import TypeVarTuple


num = float(input("enter an number: "))

if float(int(num)) == num:
    num = int(num)
    if num>=0:

        num_fac=1
        for i in range(1,num+1):
            num_fac*=i
        print("factorial of "+str(num)+" equals "+str(num_fac))
    else:
        print("factorial of "+str(num)+" is infinity")
else:
    multiply_num=1
    while True:

        if num<1:
            y = 0.976918236569 - 0.395618213536 * num + 0.428499421296 * num**2
            y=y*multiply_num

            print("factorial of "+str(round(num, 2))+" is ~"+str(round(y, 2)))
            exit()
        
        multiply_num *= num
        num -=1








