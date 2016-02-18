def encode(char):
    binchar=str(bin(ord(char)))[2:]
    while len(binchar)<7:
        binchar='0'+binchar
    chuck=''
    count=0
    zw=[]
    sent=binchar[0]
    for num in binchar:
        if num!= sent:
            if sent=='0':
                chuck+='00 '
            else:
                chuck+='0 '
            for i in range(count):
                chuck+='0'
            chuck+=' '
            sent = num
            count = 1
        else:
            count+=1
    if sent=='0':
        chuck+='00 '
    else:
        chuck+='0 '
    for i in range(count):
        chuck+='0'
    chuck+=' '
    return(chuck)
 
message = input()
norris=''
for c in message:
    chuckn=encode(c)
    nor=norris.split()
    try:
        if chuckn.split()[0]==nor[len(nor)-2]:
            x=(len(nor[len(nor)-2])+1)
            chuckn=chuckn[x:]
            norris=norris[:len(norris)-1]
    except:
        pass
    norris+=chuckn

print(norris[:len(norris)-1])

#Thanks Nathan