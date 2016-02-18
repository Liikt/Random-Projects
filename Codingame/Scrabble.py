w = []

n = int(input())
for i in range(n):
    z = [-1]
    z.append(input())
    w.append(z)
letters = input()

points = [[1, 'e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'],[2, 'd','g'],[3, 'b','c','m','p'],[4, 'f','h','v','w','y'],[5, 'k'], [8, 'j''x'], [10, 'q','z']]

def validate(word):
    global letters
    p = 0
    for x in word:
        if word.count(x) > letters.count(x):
            return -1
        else:
            for pts in points:
                if x in pts:
                    p+=pts[0]
    return p
    
for x in w:
    x[0] = validate(x[1])

maxi=w[0]
for x in w:
    if x[0] > maxi[0]:
        maxi = x
    
    
print(maxi[1])