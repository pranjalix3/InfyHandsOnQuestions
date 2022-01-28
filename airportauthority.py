n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
t = int(input())
s = 0
for i in w:
    s = s+1
    if i>t:
        s = s+1
print(s)        
        