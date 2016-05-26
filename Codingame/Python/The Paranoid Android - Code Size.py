z=input;o=int;n,w,n,n,e,n,n,u=[o(i) for i in z().split()];v=[];a=['LEFT','BLOCK','WAIT','RIGHT']
for i in range(u):
    v.append([o(j) for j in z().split()])
v.sort()
while True:
    f,p,d=z().split();f=o(f);p=o(p)
    try:
        if p<v[f][1] and d==a[0]:
            print(a[1])
        elif p>v[f][1] and d==a[3]:
            print(a[1])
        else:
            print(a[2])
    except:
        if p<e and d==a[0]:
            print(a[1])
        elif p>e and d==a[3]:
            print(a[1])
        else:
            print(a[2])
