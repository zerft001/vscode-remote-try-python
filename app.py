#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

#generate function game
def game():
    #generarate array variable
    options = ["rock", "paper", "scissors"]

    #generate input user variable
    print("Welcome to Rock, Paper, Scissors! Please enter your choice from the following options: rock, paper, scissors")
    user1 = input("Player 1, please enter your choice: ")
    if user1 not in options:
        print("Invalid choice. Please try again.")
        return game()
    user2 = input("Player 2, please enter your choice: ")
    if user2 not in options:
        print("Invalid choice. Please try again.")
        return game()
    
    #generate if statement to determine winner
    print("Rock, paper, scissors, shoot!")
    print(f"Player 1 chose: {user1} and Player 2 chose: {user2}")
    if user1 == user2:
        print("It's a tie!")
    elif user1 == "rock" and user2 == "scissors":
        print("The rock beats the scissors (breaks them), Player 1 wins!")

    elif user1 == "rock" and user2 == "paper":
        print("Paper beats stone (wraps it), Player 2 wins!")

    elif user1 == "paper" and user2 == "rock":
        print("Paper beats stone (wraps it), Player 1 wins!")

    elif user1 == "paper" and user2 == "scissors":
        print("Scissors have won over paper (they cut it), Player 2 wins!")

    elif user1 == "scissors" and user2 == "paper":
        print("Scissors have won over paper (they cut it), Player 1 wins!")

    elif user1 == "scissors" and user2 == "rock":
        print("The rock beats the scissors (breaks them), Player 2 wins!")

    else:
        print("Something went wrong. Please try again.")
        return game()
    
game()
