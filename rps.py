import numpy as np
print("1 = rock, 2 = paper, 3 = scissors")


user_choice = int(input("Enter your choice (1, 2, 3): "))
computer_choice = np.random.randint(1, 4)

if user_choice not in [1, 2, 3]:
    print("Invalid choice, please enter 1, 2, or 3.")
elif user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 1 and computer_choice == 2:
    print("Paper beats rock, you lose!")
elif user_choice == 1 and computer_choice == 3:
    print("Rock beats scissors, you win!")
elif user_choice == 2 and computer_choice == 1:
    print("Paper beats rock, you win!")
elif user_choice == 2 and computer_choice == 3:
    print("Scissors beats paper, you lose!")
elif user_choice == 3 and computer_choice == 1:
    print("Rock beats scissors, you lose!")
elif user_choice == 3 and computer_choice == 2:
    print("Scissors beats paper, you win!")
