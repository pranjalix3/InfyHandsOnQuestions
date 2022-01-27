n = int(input())
m = list(map(int,str(n)))
l = list(map(int,str(n)))
j = len(l)-1
for i in range(0,(len(l))//2):
    if l[i]!=l[j]:
        l[j]=l[i]    
    j=j-1       
k = len(l)//2    
if(len(l)%2==0):  
    l[k-1] = l[k-1]+1
    l[k] = l[k]+1
else:
    if m[k-1]<m[k+1]:
        l[k]=l[k]+1
for i in l:
    print(i,end="")   



