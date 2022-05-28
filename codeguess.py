""" a simple program that lets the user guess a given password"""

import random
from re import L, T, U
import re


def level(level):
    
    if level == "hard":
        print("you are on Hard mode")
        return 9
    
    elif level == "easy":
        print("you are on easy mode")
        return 4
    
    elif level == "normal":
        print("your are on normal mode")
        return 6
        

def code(size):
    """
    this function generates random numbers
    -returns a list of generated numbers 
    -from 1 to 9
    """
    
    str_code = ""
    
    for i in range(size):
        str_code += str(random.randint(1,9))

    return str_code


def get_user_input(prompt):
    """a simple function that takes input from terminal
    - returns the user input
    """
    user_input = input(prompt)
    
    return user_input
    
    
def validate_user_input(user_input):
    """
    this function is for validating user_input
    returns true if user input is a digit
    """
    
    if user_input.isdigit() != True:
        return False
    
    return True


def correct_guess(guess, code):
    
    if(code == guess):
        return True
    
    else:
        return False


def give_clue(guess, code):
    
    found = []
    found_in_correct_position = []
    
    for num in guess:
        if num in code:
            # print("we found something")
            found.append(num)
    
    for index, num in enumerate(guess):
        
        if code[index] == guess[index]:
            found_in_correct_position.append(num)
            # print("my boiii")
            
    
    if len(found) > 0:
        print("we found something")

    print("\n we found these exist: ",found, "\n and we found these: ",
        found_in_correct_position," in the correct place\n")
    return False


def run_main(code):
    """
    this function runs the the program logic
    """
        
    tries = 11;
    
    while(True):
        
        if tries == 0:
            print("game over!!!")
            break
        
        user_input = get_user_input("Enter a number from 1 to 9 to guess code:\n")
        
        if correct_guess(user_input, code):
            print("YOU ARE IN!!!")
            break
        
        if validate_user_input(user_input) == False:
            print("\n> Oops you have some invalid characters try again:")
            print(f"> --WARNING!!! YOU HAVE ({tries}) TRIES LEFT---")
            tries -=1
            
        
        elif validate_user_input(user_input) == True:
            print("\n> You might be on to something")   
                    
        give_clue(user_input, code)
     
  
  
def game_opp():
    
    return """Choose game level
-easy
-normal
-hard\n"""
  

if __name__ == '__main__':
    
    print(game_opp())
    
    game_level = get_user_input("Enter game level: ")
    
    level = level(game_level)
    
    code = code(level)
    print(code)
    run_main(code)



