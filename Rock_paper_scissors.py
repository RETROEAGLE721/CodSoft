import random
import time

round_tracking = "00"
user_selection_option = {'1':'Rock', '2':'Paper', '3':'Scissors'}
priority = {'Rock':'Paper', 'Paper':'Scissors','Scissors':'Rock'}
while True:
    print("Select your choice from given options")
    print("1. Rock  2. Paper  3. Scissors")
    user_input = input()
    if user_input == "0":
        break
    if user_input != '1' and user_input != '2' and user_input != '3':
        print("Please select from given options and try again")
        time.sleep(2)
        continue
    user_input = user_selection_option[user_input]
    com_input = random.choice(["Rock","Paper","Scissors"])
    if user_input == com_input:
        print("It's a tie")
    elif priority[user_input] == com_input:
        print("Computer Wins")
        round_tracking = str(int(round_tracking[0])+1)+round_tracking[-1]
    else:
        round_tracking = round_tracking[0]+str(int(round_tracking[-1])+1)
        print("You Win")
    print()
    print("Round Wins")
    print("Your wins:-",round_tracking[-1])
    print("Computer wins:-",round_tracking[0])
    play_again = input("Do your want to play again?[Yes/No] :-")
    if play_again == "Yes" or play_again == "yes":
        pass
    else:
        print("Thanks for playing. Have a nice day.")
        break
exit()