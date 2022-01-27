s = str(input())
l = list(s)
k = []
for i in l:
    if i.isdigit():
        k.append(i)
k.sort(reverse=True)
c=0
m=0
n=0
le = len(k)
for i in range(le-1,-1,-1):
    if int(k[i])%2==0:
        c=1
        m = i
        n = k[le-1]
        k[le-1]=k[i]
        break        
if c==0:
    print(-1)
else:
    for i in range(m,len(k)):
        if m == len(k)-2:
            k[m]=n 
            break
        else:
            k[m]=k[m+1]
    for i in k:
        print(i,end="")            


         




