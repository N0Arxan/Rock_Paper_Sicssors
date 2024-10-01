import sys
import random

wins = 0
loses = 0
ties = 0
RPS=['Rock','Paper','Sicssors']
print('\n Rock Paper Sicssors \n')

while True :
    
    print("wins=%s losses=%s tie=%s \n" %(wins , loses ,ties))
    #player move while 
    while True :
        player_move = input("enter (R)ock , (P)aper  (S)icssors and for (Q)uit \n")
        if player_move == "Q" :
            sys.exit()
        elif player_move == "R" :
            player_move = "Rock"
            break
        elif player_move == "P" :
            player_move = "Paper"
            break
        elif  player_move == "S" :
            player_move = "Sicssors"
            break
        else:
            continue
    print(player_move , " Vs ....")

    machine_move = random.choice(RPS)
    
    #logic 
    if player_move == machine_move :
        print(machine_move, "\n\nthis is a tie Bro calm down \n")
        ties += 1
        continue
    else:
        if player_move == "Rock" and machine_move == "Paper" :
            print(machine_move, "\n\nthis is lose maybe next time losser \n")
            loses += 1
            continue
        elif player_move == "Rock" and machine_move == "Sicssors" :
            print(machine_move, "\n\nits very Rare but you won congrats \n")
            wins += 1
            continue
        elif player_move == "Paper" and machine_move == "Sicssors" :
            print(machine_move, "\n\nthis is lose maybe next time losser \n")
            loses += 1
            continue
        elif player_move == "Paper" and machine_move == "Rock" :
            print(machine_move, "\n\nits very Rare but you won congrats\n ")
            wins += 1
            continue
        elif player_move == "Sicssors" and machine_move == "Rock" :
            print(machine_move, "\n\nthis is lose maybe next time losser \n")
            loses += 1
            continue
        elif player_move == "Sicssors" and machine_move == "Paper" :
            print(machine_move, "\n\nits very Rare but you won congrats \n")
            wins += 1
            continue
