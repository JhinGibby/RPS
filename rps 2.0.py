import numpy as np

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in choices:
        user_input = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return user_input

def get_computer_choice():
    return np.random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_input = get_user_choice()
    comp_choice = get_computer_choice()

    print(f"You chose: {user_input}")
    print(f"Computer chose: {comp_choice}")

    result = determine_winner(user_input, comp_choice)
    print(result)

if __name__ == "__main__":
    main()
