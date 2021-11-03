import random 

print("Winning Rules of the Colors choices Game as follows:\n")
print("Enter a name of a color and match computer choice to Win the computer.") 

computer_score = 0
player_score = 0 
   
while True:
#Declare colors choices as variables and specify colors of the game inside the nested while loop.
    print("select a color:")
    print("red", "yellow", "orange", "green", "blue\n", sep='\t') 
    player_choice = str(input("Choose a color: "))
    while player_choice != "red" and player_choice != "yellow" and player_choice != "orange" and player_choice != "green" and player_choice != "blue":
        print("red", "yellow", "orange", "green", "blue\n", sep='\t') 
        player_choice= str(input("enter valid input: "))
#The random module’s randint function to get an integer between zero and four, 
#and compare in the list of colors for the choice of the computer's color.
    computer_choice = random.randint(0,4)
    colors =["red", "yellow", "orange", "green", "blue"]
    for index, item in enumerate(colors):
        if index == computer_choice:
            computer_choice = item
#Compare their inputs with the choice of the computer.
    if player_choice == computer_choice:
        print("Computer color choice is: " + computer_choice + "\n") 
        print("The user has won.\n")
        player_score += 1
        print("score player's=")
        print("player score: "+str(player_score), "computer score: "+str(computer_score), sep='\n', end='\n')
    else:
#Compare their inputs with the choice of the computer.
        print("Computer color choice is: " + computer_choice + "\n") 
        print("The computer has won.\n")
        computer_score += 1
        print("score player's=")
        print("player score: "+str(player_score), "computer score: "+str(computer_score), sep='\n', end='\n')
#Ask if players want to play again.
        answer=str(input("Do you want to play again Yes(y) or No(n):"))
        if answer =='n'or answer =='N':
            print("\nThanks for playing")
            break
# after coming out of the while loop 
# we print thanks for playing and the overall result of the game.
if computer_score == player_score:
    print("Game is Tied")
    print("\nThanks for playing") 
elif computer_score < player_score:
    print("Player is Victorious")
    print("<== User wins ==>")
    print("\nThanks for playing")
elif computer_score > player_score:
    print("\n<== Computer wins ==>")
    print("\nPlayer is Defeated")
    print("\nThanks for playing") 