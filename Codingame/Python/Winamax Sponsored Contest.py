import sys
import math
pton={'J':11, 'Q':12, 'K':13, 'A':14}
faces=['J', 'Q', 'K', 'A']

def fight():
    global pxcards
    
    if len(pxcards[0])!=0 and len(pxcards[1])!=0:   
        fight=True
        trade=[[],[]]   
        while fight==True:
            p1c,p2c=-1,-1   
            if pxcards[0][0] not in faces:
                p1c=int(pxcards[0][0])
            else:
                p1c=pton[pxcards[0][0]]
            if pxcards[1][0] not in faces:
                p2c=int(pxcards[1][0])
            else:
                p2c=pton[pxcards[1][0]]
            
            trade[0].append(pxcards[0][0])
            pxcards[0].pop(0)
            trade[1].append(pxcards[1][0])
            pxcards[1].pop(0)           
            if p1c>p2c: 
                for p in range(2):
                    for card in trade[p]:
                        pxcards[0].append(card)
                fight=False
            elif p2c>p1c:
                for p in range(2):
                    for card in trade[p]:
                        pxcards[1].append(card)
                fight=False
            else:           
                for i in range(2):
                    for j in range(3):      
                        if len(pxcards[i])!=0:  
                            trade[i].append(pxcards[i][0])
                            pxcards[i].pop(0)
                        else:
                            return 0
        if len(pxcards[0])==0:
            return 2
        elif len(pxcards[1])==0:
            return 1
        else:
            return -1
                        
winner=-1
n = int(input())  
pxcards=[[],[]]
for i in range(n):
    card=input()
    pxcards[0].append(card[:len(card)-1])
m = int(input())  
for i in range(m):
    card=input()
    pxcards[1].append(card[:len(card)-1])

rounds=0
while winner==-1:
    winner=fight()
    rounds+=1
if (winner==0):
    print('PAT')
else:
    print(str(winner)+' '+str(rounds))
