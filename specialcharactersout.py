s = str(input())
l = list(s)
e = []
o = []
ans = []
c=0
for i in range(0,len(l)):
    if l[i].isdigit():
        if int(l[i])%2==0:
            e.append(l[i])
        else:
            o.append(l[i])
    elif l[i].isalpha():
        continue
    else:
        c+=1    
if(c%2==0):
    i = 0
    j = 0
    while(i<len(e) and j<len(o)):
        ans.append(e[i])
        ans.append(o[j])
        i+=1
        j+=1
    if(i!=len(e)):
        while(i<len(e)):
            ans.append(e[i])
            i+=1
    if(j!=len(o)):
        while(j<len(o)):
            ans.append(o[j])
            j+=1 
else:
    i = 0
    j = 0
    while(i<len(e) and j<len(o)):
        ans.append(o[j])
        ans.append(e[i])
        i+=1
        j+=1
    if(i!=len(e)):
        while(i<len(e)):
            ans.append(e[i])
            i+=1
    if(j!=len(o)):
        while(j<len(o)):
            ans.append(o[j])
            j+=1 
for p in ans:
    print(p,end="")            

            
        


       