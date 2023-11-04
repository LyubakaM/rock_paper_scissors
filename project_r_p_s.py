import random
score_player1 = 0
score_cpu = 0
timer = 0
while True:
    if timer > 30:
        print("Too much games for today!Take a rest or have some snacks!")
        break
    player_choice = input("Choose [R]ock, [P]aper, or [S]cissors: ")
    timer += 1
    if player_choice == "end":
        break
    elif player_choice.lower() == "r":
        player_choice = "rock"
    elif player_choice.lower() == "p":
        player_choice = "paper"
    elif player_choice.lower() == "s":
        player_choice = "scissors"
    else:
        raise SystemExit("Invalid Input. Try Again...")
    random_computer_number = random.randint(1, 3)
    computer_move = ""
    if random_computer_number == 1:
        computer_move = "rock"
    elif random_computer_number == 2:
        computer_move = "paper"
    elif random_computer_number == 3:
        computer_move = "scissors"

    if (computer_move == "scissors" and player_choice == "rock") or (computer_move == "paper" and player_choice == "scissors") \
            or (computer_move == "rock" and player_choice == "paper"):
        score_player1 += 1
        print(f"You win!AI's choice is {computer_move}")
        print(f"Score: Player - {score_player1} CPU - {score_cpu}")
        print("If you want to end the game type end")
        print()
        print()
        print()

    elif computer_move == player_choice:
        print(f"Draw!AI's choice is {computer_move}")
        print(f"Score: Player - {score_player1} CPU - {score_cpu}")
        print("If you want to end the game type end ")
        print()
        print()
        print()

    else:
        score_cpu += 1
        print(f"You loose!AI's choice is {computer_move}")
        print(f"Score: Player - {score_player1} CPU - {score_cpu}")
        print("If you want to end the game type end ")
        print()
        print()
        print()


