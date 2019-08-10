n=100
a=['c' for i in range(0,n)]

for i in range(1,n+1):
    for j in range(i,n+1,i):
        if a[j-1]=='c':
            a[j-1]='o'
        elif a[j-1]=='o':
            a[j-1]='c'
            
for i in range(len(a)):
    if a[i]=='o':
        print(i+1)
