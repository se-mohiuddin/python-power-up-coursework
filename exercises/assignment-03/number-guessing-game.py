'''
Question-1:
Write a Python program that lets a user guess a secret number between 1 and 100. 
The program should provide hints whether the guessed number is too high or too low, and it should continue until the correct number is guessed.

Instructions:
1.	The computer selects a random number between a specified range (e.g., 1 to 100).
2.	You start by guessing a number within that range.
3.	The game tells you whether your guess is too high or too low.
4.	You continue guessing numbers based on the feedback until you guess the correct number.
5.	The game displays the number of attempts it took you to guess correctly.
'''
import random
print("------Guess Number Game------")
#1)
c_num=random.randrange(1,101)
guess_num=0
count=0
while guess_num!=c_num:
    guess_num=int(input("Guess a number between 1 -to- 100:  "))
    print()
    if guess_num > 100 or guess_num < 1:
        print("The number is out of range! (0-100)")
        print("--------------------------------------------------")
        continue
    elif guess_num > c_num:
        print("The guess is too high")
        print("Think lower than this")
        print("--------------------------------------------------")
    elif guess_num < c_num:
        print("The guess is too low")
        print("Think higher than this")
        print("--------------------------------------------------")

    count+=1

print("Congratulations you have guessed the correct number", c_num)
print("You took", count, "attempts to guess correctly")
print("####################################################")