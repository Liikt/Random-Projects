import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rounds = -1
player1 = ''
player2 = ''
war = ''
sent = 0

def aRound():
    global rounds
    global player1 
    global player2 
    global war 
    global sent
    
    print('ROUND ' + str(rounds) + ' FIGHT', file=sys.stderr)
    print('Player 1: ' + player1, file=sys.stderr)
    print('Player 2: ' + player2, file=sys.stderr)
    
    
    if len(player1) == 0 and len(player2) == 0:
        print('PAT')
        sent = 1
        return
    elif len(player1) == 0:
        print('2 ' + str(rounds))
        sent = 1
        return
    elif len(player2) == 0:
        print('1 ' + str(rounds))
        sent = 1
        return
    
    wert1 = player1[0]
    wert2 = player2[0]

    p1 = wert1
    p2 = wert2
    
    war = war + p1 + p2

    player1 = player1[1:]
    player2 = player2[1:]

    if wert1 == '1':
        wert1 += '0'
    elif wert1 == 'J':
        wert1 = '11'
    elif wert1 == 'Q':
        wert1 = '12'
    elif wert1 == 'K':
        wert1 = '13'
    elif wert1 == 'A':
        wert1 = '14'
    if wert2 == '1':
        wert2 += '0'
    elif wert2 == 'J':
        wert2 = '11'
    elif wert2 == 'Q':
        wert2 = '12'
    elif wert2 == 'K':
        wert2 = '13'
    elif wert2 == 'A':
        wert2 = '14'

    if int(wert1) > int(wert2):
        player1 = player1 + war
        war = war[:2]
    elif int(wert2) > int(wert1):
        player2 = player2 + war
        war = war[:2]
    elif int(wert1) == int(wert2):
        if len(player1) < 3 and len(player2) > 3:
            print('PAT ' + str(rounds))
            sent = 1
            return
        elif len(player2) < 3 and len(player1) > 3:
            print('PAT ' + str(rounds))
            sent = 1
            return
        elif len(player1) < 3 and len(player2) < 3:
            print('PAT ' + str(rounds))
            sent = 1
            return
        else:
            war = war + p1 + player1[0] + player1[1] + player1[2]
            war = war + p2 + player2[0] + player2[1] + player2[2]
        player1 = player1[3:]
        player2 = player2[3:]
        print('Player 1: ' + player1, file=sys.stderr)
        print('Player 2: ' + player2, file=sys.stderr)
        print('War: ' + war, file=sys.stderr)
        
        if len(player1) < 3 or len(player2) < 3:
            print('PAT')
            sent = 1
            return
        
        aRound()
    print('War: ' + war, file=sys.stderr)
    print('.......................................', file=sys.stderr)
    war = ''
    

n = int(input())  # the number of cards for player 1
for i in range(n):
    player1 = input()[0] + player1 # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    player2 = input()[0] + player2  # the m cards of player 2



#print(player1[:1], file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

while sent == 0:
    rounds += 1
    aRound()
    