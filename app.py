#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

#generate dictionary for players score
score = {"Player 1": 0, "Player 2": 0}
#generate function game
def game(score):
    #generate array for options
    options = ["rock", "paper", "scissors"]

    while True:
        #generate input user variable
        print("Welcome to Rock, Paper, Scissors! Please enter your choice from the following options: rock, paper, scissors")
        user1 = input("Player 1, please enter your choice: ").lower()
        if user1 not in options:
            print("Invalid choice. Please try again.")
            return game()
        user2 = input("Player 2, please enter your choice: ").lower()
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
            score["Player 1"] += 1

        elif user1 == "rock" and user2 == "paper":
            print("Paper beats stone (wraps it), Player 2 wins!")
            score["Player 2"] += 1

        elif user1 == "paper" and user2 == "rock":
            print("Paper beats stone (wraps it), Player 1 wins!")
            score["Player 1"] += 1

        elif user1 == "paper" and user2 == "scissors":
            print("Scissors have won over paper (they cut it), Player 2 wins!")
            score["Player 2"] += 1

        elif user1 == "scissors" and user2 == "paper":
            print("Scissors have won over paper (they cut it), Player 1 wins!")
            score["Player 1"] += 1

        elif user1 == "scissors" and user2 == "rock":
            print("The rock beats the scissors (breaks them), Player 2 wins!")
            score["Player 2"] += 1

        else:
            print("Something went wrong. Please try again.")
            return game()
        
        
        print(f"Player 1 score: {score['Player 1']}")
        print(f"Player 2 score: {score['Player 2']}")
    
        #the user select play again or not if not the game is over and terminate the while bucle
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == "y":
            return game(score)
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            return
    
    #print the winner and final score for the players
    if score["Player 1"] > score["Player 2"]:
        print("Player 1 wins!")
    elif score["Player 1"] < score["Player 2"]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
    print(f"Final score: Player 1 score: {score['Player 1']} vs Player 2 score: {score['Player 2']}")
game(score)
