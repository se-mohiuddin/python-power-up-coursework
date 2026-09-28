'''
Question-2:Leap Year Checker 
Write a program that asks the user to input a year and determines whether the year is a leap year or not. A leap year is either divisible by 4 but not by 100, or divisible by 400.
'''

year=int(input("Enter the year number to check if it is leap or not: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This year is leap year")
else:
    print("This year is not leap year")