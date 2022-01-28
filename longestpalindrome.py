n=(input())
ara=[]
ans =[]
d={}
for i in range(len(n)):
    for j in range(i,len(n)):
        x=n[i:j+1]
        ara.append(x)
for i in range(0,len(ara)):
    k = len(ara[i])-1
    c=0
    for j in range(0,(len(ara[i])//2)):
        if(ara[i][j]==ara[i][k]):
            k=k-1
            continue
        else:
            c=1
            break
    if c==0:
        ans.append(ara[i])
for i in ans:
    if i not in d:
        d[i] = len(i)
    else:
        d[i]+=1
m=0      
s = ""  
for key,values in d.items():
    if(values>m):
        m = values 
        s = key 
print(s)        




