""" a simple program that lets the user guess a given password"""

import random
from re import L, T, U
import re


def level(level):
    """this is the function for indicating dificulty level

    Args:
        level (string): indicates the duficulty level { easy, normal, hard}

    Returns:
        (integer) : an integer  
    """
    
    if level == "hard":
        print("you are on Hard mode")
        return 9
    
    elif level == "easy":
        print("you are on easy mode")
        return 4
    
    elif level == "normal":
        print("your are on normal mode")
        return 6
    
    else:
        return False
        

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
    """_summary_

    Args:
        guess (string): it is the guess/ user input 
        code (string): the generated code/ random numbers

    Returns:
        _boolean: true if the code is equal to guess
                - false if they are not 
    """
    
    if(code == guess):
        return True
    
    else:
        return False


def give_clue(guess, code):
    """this function gives the user clues

    Args:
        guess (string): the guess is the user input
        code (string): the code
    """
    
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
    
    # return False



def run_main(code):
    """
    this function runs the the program logic
    """
        
    tries = 11;
    
    while(True):
        
        if tries == 0:
            print("game over!!!")
            break
        
        user_input = get_user_input(f"Enter a number from 1 to {len(code)} to guess code:\n")
        
        # while len(user_input) > len(code):
        #     print("incorrect len")
        #     get_user_input(f"Enter a number from 1 to {len(code)} to guess code:\n")
        
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
  

def handle_level_input():
    
    
    list_of_levels =  ["hard", "easy", "normal"]
    while True:
        get_game_level = get_user_input("Enter game level: ")
        
        if get_game_level in list_of_levels:
            get_level = level(get_game_level)
            return get_level
            



if __name__ == '__main__':
    
    print(game_opp())
    
    # game_level = get_user_input("Enter game level: ")
    
    # level = level(game_level)
    
    
    
    code = code(handle_level_input())
    print(code)
    run_main(code)



