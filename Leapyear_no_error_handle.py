#Author: Cyrus Swihart
#CS 362 HW 1 Problem 4: leap year Calculator

'''
INSTRUCTIONS: To run, open a terminal and type 'python .\Cyrus_Swihart_hw1.py'.
Then, the program will start and ask you for input. Type in integers ONLY. The program 
tells you whether or not the year is a leap year.
'''

def yes(n):
    print(str(n) + " is a leap year")

def no(n):
    print(str(n) + " is NOT a leap year")

n = int(input("Enter a year: "))

if n % 400 == 0:
    yes(n)
    exit(1)
if n % 100 == 0:
    no(n)
    exit(1)
if n % 4 == 0:
    yes(n)
    exit(1)
no(n)

