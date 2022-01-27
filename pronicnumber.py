
n=(input())

ara=[]
for i in range(len(n)):
    for j in range(i,len(n)):
        x=n[i:j+1]
        ara.append(x)
s=set()
for i in ara:
    for j in range(1,(int(i)//2)+1): 
        if int(j)*(int(j)+1)==int(i):
            s.add(int(i))     
            break   
x=(sorted(s))
values = ','.join(map(str, x))
values=values.replace(',',' ')
print(values)

