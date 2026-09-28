#main-hangman.py
'''
Question-2:
Guess the hidden word by suggesting letters one at a time. You have a limited number of attempts before the "hangman" is complete.

Instructions:
1.	The computer selects a random word from a predefined list.
2.	The game displays the number of letters in the word as underscores, representing unguessed letters.
3.	You guess a letter by entering it.
4.	If the guessed letter is in the word, the corresponding underscores are replaced with the letter.
5.	If the guessed letter is not in the word, a part of the hangman is drawn (e.g., head, body, arms, legs).
6.	You continue guessing letters until you either guess the word correctly or the hangman is fully drawn.
7.	If you guess the word, you win! If the hangman is fully drawn before you guess the word, you lose.
'''
import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display.append('_')

end_of_game = False
lives = len(stages) - 1

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(guess, "is not in the word you have lost a life")
        print(lives, "lives are remaining")

    if '_' not in display:
        end_of_game = True
        print("Congratulations! You win!")
    elif lives == 0:
        end_of_game = True
        print("Sorry, you lose. The word was:", chosen_word)

    print(' '.join(display))

