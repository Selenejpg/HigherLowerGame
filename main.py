import art
import game_data
import random
import os

from art import logo
from art import vs

from game_data import data

def random_character():
    character = random.choice(data)
    return character

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
print(logo)

def higher_lower():
    counter = 0
    continue_playing = True  
    
    while continue_playing:
        characters = [random_character(), random_character()]
        
        a, b = characters  

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

        choice = input("Who has more followers? Type 'A' or 'B': ")

        if (choice == "A" and a['follower_count'] > b['follower_count']) or (choice == "B" and b['follower_count'] > a['follower_count']):
            counter += 1
            cls()
            print(f"You are right! Your current score is {counter}")
            print("\n------------------------------------------------\n")
            
        else:
            print(f"Sorry, that's wrong. Final score: {counter}")
            continue_playing = False

    return counter

play_again = 'y'  
while play_again == 'y':
    score = higher_lower()
    play_again = input("Do you want to play again? Write 'y' if you want to continue or 'n' if you want to stop: ")
    if play_again == "y":
        cls()
