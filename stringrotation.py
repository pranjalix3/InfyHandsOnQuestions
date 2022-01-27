inp=input()
l=inp.split(",")
for i in l:
    s=""
    s1=i.split(":")
    n = len(s1[0])
    k = list(map(int,str(s1[1])))
    sum=0
    for i in k:
        sum = sum + (i*i)
    if sum%2==0:
        s= s+ s1[0][-1:]
        s = s+ s1[0][0:n-1]
    else:
        s =s + s1[0][2:n]
        s = s+ s1[0][0:2]
    print(s)    
