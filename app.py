# prompt the player if they want to play Rock Paper Scissors
# if yes, prompt the player to make a choice
# if no, thank the player and end the game

from random import choice

print("Welcome to Rock Paper Scissors!")
play = input("Do you want to play? (yes/no): ")
# validate input
while play not in ["yes", "no"]:
    print("Invalid choice. Please choose yes or no.")
    play = input("Do you want to play? (yes/no): ")

# keep track of player and computer scores
player_score = 0
computer_score = 0
ties = 0

while play == "yes":

    player = input("Choose rock, paper, or scissors: ")
    # validate player input
    while player not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player = input("Choose rock, paper, or scissors: ")
    computer = choice(["rock", "paper", "scissors"])

    print(f"Computer chose {computer}")

    if player == computer:
        print("It's a tie!")
        ties += 1
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    play = input("Do you want to play again? (yes/no): ")
    # validate input
    while play not in ["yes", "no"]:
        print("Invalid choice. Please choose yes or no.")
        play = input("Do you want to play again? (yes/no): ")

print("Thank you for playing Rock Paper Scissors!")
# print final scores in a single line
print(f"Player: {player_score}, Computer: {computer_score}, Ties: {ties}")