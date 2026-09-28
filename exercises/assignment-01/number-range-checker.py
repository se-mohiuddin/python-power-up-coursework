'''
Question-1: Number Range Checker 
Write a program that prompts the user to enter a number. Check whether the number falls within any of the following ranges:
0-10: "Low Range"
11-50: "Medium Range"
51-100: "High Range"
Outside of 0-100: "Out of Range"
'''
n=int(input("Enter a number ranges from 0-100:  "))

if n>= 0 and n <=10:
    print("The entered value is in Low Range")
elif n>= 11 and n <=50:
    print("The entered value is in Medium Range")
elif n>= 51 and n <=100:
    print("The entered value is in High Range")
else:
    print("The entered value is out of range")

