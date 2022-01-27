l = list(map(int,input().split(',')))
sum =0
k = []
ans =[]
for i in l:
    if i == 0:
        sum = 0
        k.append(sum)
    else:
        for j in range(2,i):
            if i%j ==0:
                sum = sum +j
        k.append(sum+1) 
for i in k:
    if i in l:
        ans.append(i)
for i in ans:
    print(i,end=",")


