inp=input()
l=inp.split(",")
s=""
for i in l:
    c=0
    s1=i.split(":")
    n=str(len(s1[0]))
    if n in s1[1]:
        x=int(n)
        s+=s1[0][x-1]
        c+=1
    else:
        x=int(n)
        for each in range(x-1,-1,-1):
            if str(each) in s1[1]:
                s+=s1[0][each-1]
                c+=1 
                break
    if c==0:
        s+="X"
                
print(s)