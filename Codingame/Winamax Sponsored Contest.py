import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rounds = -1
player1 = ''
player2 = ''
war = ''
sent = 0
dic = {'1':'10', 'J':'11', 'Q':'12', 'K':'13', 'A':'14'}

def aRound():
    global rounds
    global player1 
    global player2 
    global war 
    global sent
    
    print('ROUND ' + str(rounds) + ' FIGHT', file=sys.stderr)
    print('Player 1: ' + player1, file=sys.stderr)
    print('Player 2: ' + player2, file=sys.stderr)
    
    if len(player1) == 0:
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
    
    war = p1 + p2

    player1 = player1[1:]
    player2 = player2[1:]

    if wert1 == '1' or wert1 == 'J' or wert1 == 'Q' or wert1 == 'K' or wert1 == 'A':
        wert1 = dic[wert1]
    if wert2 == '1' or wert2 == 'J' or wert2 == 'Q' or wert2 == 'K' or wert2 == 'A':
        wert2 = dic[wert2]

    if int(wert1) > int(wert2):
        player1 = player1 + war
        war = war[:len(war)-2]
    elif int(wert2) > int(wert1):
        player2 = player2 + war
        war = war[:len(war)-2]
    elif int(wert1) == int(wert2):
        war = war[:len(war)-2]
        war = war + p1 + player1[0] + player1[1] + player1[2] + p2 + player2[0] + player2[1] + player2[2]
        player1 = player1[3:]
        player2 = player2[3:]
        print('Player 1: ' + player1, file=sys.stderr)
        print('Player 2: ' + player2, file=sys.stderr)
        print('War: ' + war, file=sys.stderr)
        
        if len(player1) == 0 or len(player2) == 0:
            print('PAT')
            sent = 1
            return
        
        aRound()
    print('War: ' + war, file=sys.stderr)
    print('.......................................', file=sys.stderr)
    war = ''
    

n = int(input())  # the number of cards for player 1
for i in range(n):
    player1 = player1 + input()[0] # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    player2 = player2 + input()[0]  # the m cards of player 2



#print(player1[:1], file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

while sent == 0:
    rounds += 1
    aRound()
    