import random
play = input("Do you want to play a game of Rock Paper Scissors? (yes/no)")
global draws, wins, defeats, timesPlayed, rockChoices, paperChoices, scissorChoices
draws, wins, defeats, timesPlayed, rockChoices, paperChoices, scissorChoices = 0, 0, 0, 0, 0, 0, 0
while play == "yes":


    timesPlayed = timesPlayed + 1
    rps = ["rock", "paper", "scissors"]
    compChoice = random.choice(rps)

    choice = input("Enter your choice: ")
    print("You chose " + choice)
    if choice.lower() == compChoice:
        print("Computer chose " + compChoice)
        print("Game is a draw")
        draws += 1

    elif choice.lower() == "rock" and compChoice == "paper":
        print("Computer chose " + compChoice)
        print("You lose!")
        defeats += 1

    elif choice.lower() == "scissors" and compChoice == "rock":
        print("Computer chose " + compChoice)
        print("You lose!")
        defeats += 1

    elif choice.lower() == "paper" and compChoice == "scissors":
        print("Computer chose " + compChoice)
        print("You lose!")
        defeats += 1

    elif choice.lower() != "paper" and choice.lower() != "rock" and choice.lower() != "scissors":
        print("Play properly!")

    else:
        print("Computer chose " + compChoice)
        print("You win!")
        wins += 1


    print("Do you want to play again? (yes/no)")
    playAgain = input()
    if playAgain == "no":
        print("Thank you for playing")
        txt = "You won {} out of the {} games you played"
        print(txt.format(wins, timesPlayed))
        break









