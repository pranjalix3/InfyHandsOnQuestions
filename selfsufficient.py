n = int(input())
l = list(map(int,input().split()))
m = list(map(int,input().split()))
s1=0
s2=0
for i in l:
    s1 = s1 +i
for j in m:
    s2 = s2 + j
ans = s2-s1
if(ans<=0):
    print(-1)
else:
    print(ans)            