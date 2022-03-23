from Wordlist import words
from Hangman_stages import logo, stages
import random
import os
from time import sleep


def game():
    print("".join(logo))
    word=random.choice(words)
    lives=6
    display=[]
    for i in range(len(word)):
        display+="_"
    while True:
        char=input("Enter a character: ")
        for position in range(len(word)):
            if char==word[position]:
                display[position]=char
        if char not in word:
            print("Entered character is not present in the word\nYou lose a live")
            lives-=1
        print("".join(display))
        print(stages[7-lives-1])
        if '_' not in display:
            print("You've won the game")
            break
        elif lives==0:
            print("Player is dead\nYou lose")
            print(f"Right answer was {word}")
            break
    print(input("Press any key to Exit"))
    return


game()


