cnt=0
num=int(input())

for x in range(1,num+1):
    if(x<100):
        cnt=cnt+1
    if (x == 1000):
        continue
    elif(x>=100):
        strx=str(x)
        a,b,c=strx
        a,b,c=int(a),int(b),int(c)
        if(a+c==2*b):
            cnt=cnt+1
print(cnt)
#야매로함...