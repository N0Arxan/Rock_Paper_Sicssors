import sys
import random

wins = 0
loses = 0
ties = 0

move_dict = {
        'R': 'Rock',
        'P': 'Paper',
        'S': 'Scissors',
        'Q': 'Quit'
    }

outcome_dict = {
        'Rock': {'Rock': 'tie', 'Paper': 'lose', 'Scissors': 'win'},
        'Paper': {'Rock': 'win', 'Paper': 'tie', 'Scissors': 'lose'},
        'Scissors': {'Rock': 'lose', 'Paper': 'win', 'Scissors': 'tie'}
    }


RPS=['Rock','Paper','Scissors']


def print_status():
    print("\nRock Paper Scissors\n")
    print("wins = {} losses = {} ties = {}\n".format(wins, loses, ties))


def get_player_move():
       
       while True:
        move = input("Enter (R)ock, (P)aper, (S)cissors or (Q)uit: \n").upper()
        if move in move_dict:
            if move == 'Q':
                sys.exit()
            return move_dict[move]
        else:
            print("Invalid input, please try again.")

def get_machine_move():
    return random.choice(RPS)

def determine_winner(player_move, machine_move):
    global wins
    global ties
    global loses
    outcome = outcome_dict[player_move][machine_move]
    
    if outcome == 'tie':
        print("{}\n\nIt's a tie!\n".format(machine_move))
        
        ties += 1

    elif outcome == 'win':
        print("{}\n\nYou won! Congrats!\n".format(machine_move))
        
        wins += 1

    else:
        print("{}\n\nYou lost! Better luck next time.\n".format(machine_move))
        loses += 1

def main():
    
    print_status()
    
    while True:
        
        player_move = get_player_move()
        
        print("{} vs ....".format(player_move))
        
        machine_move = get_machine_move()
        
        determine_winner(player_move, machine_move)
        
        print_status()


main()