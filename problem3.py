#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

number = int(input("enter a number between 1 and 10: "))

if number>10:
    print("LESS THAN 10!!!!")
    exit()

total=0
for i in range(1,number+1):
    i_th_num = int("1"*i)
    total+=i_th_num

print("the sum of the series is "+str(total))