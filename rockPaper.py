"""
Rock Paper Scissors Game
A simple interactive game where the player competes against the computer.
"""

import random


def get_user_choice():
    """
    Get and validate user's choice.
    
    Returns:
        str: The user's choice (rock, paper, or scissors)
    """
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower().strip()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("❌ Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower().strip()
    return user_choice


def get_computer_choice():
    """
    Generate computer's random choice.
    
    Returns:
        str: The computer's choice (rock, paper, or scissors)
    """
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of a single round.
    
    Args:
        user_choice (str): The player's choice
        computer_choice (str): The computer's choice
        
    Returns:
        str: Result message indicating winner or tie
    """
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"


def display_result(result, user_choice, computer_choice):
    """
    Display the round result with emoji and formatted output.
    
    Args:
        result (str): The result of the round (win, lose, or tie)
        user_choice (str): The player's choice
        computer_choice (str): The computer's choice
    """
    print(f"\nYou chose: {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    
    if result == "win":
        print("🎉 You win this round!")
    elif result == "lose":
        print("💻 Computer wins this round!")
    else:
        print("🤝 It's a tie!")


def display_score(wins, losses, ties):
    """
    Display the current game score.
    
    Args:
        wins (int): Number of wins
        losses (int): Number of losses
        ties (int): Number of ties
    """
    print(f"\n{'='*40}")
    print(f"Score - Wins: {wins} | Losses: {losses} | Ties: {ties}")
    print(f"{'='*40}\n")


def play_game():
    """
    Main game loop that manages the overall game flow.
    """
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮\n")
    
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        try:
            # Get choices
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            
            # Determine and display result
            result = determine_winner(user_choice, computer_choice)
            display_result(result, user_choice, computer_choice)
            
            # Update score
            if result == "win":
                wins += 1
            elif result == "lose":
                losses += 1
            else:
                ties += 1
            
            # Display current score
            display_score(wins, losses, ties)
            
            # Ask to play again
            play_again = input("Do you want to play again? (yes/no): ").lower().strip()
            if play_again not in ['yes', 'y']:
                print(f"\n🏁 Game Over!")
                print(f"Final Score - Wins: {wins} | Losses: {losses} | Ties: {ties}")
                print("Thanks for playing! 👋\n")
                break
                
        except KeyboardInterrupt:
            print("\n\n🛑 Game interrupted by user.")
            print(f"Final Score - Wins: {wins} | Losses: {losses} | Ties: {ties}")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    play_game()
