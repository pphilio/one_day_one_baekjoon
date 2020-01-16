i=int(input())

for j in range(i):
    a = input()
    cnt = 0
    sum = 0
    for x in a:
        if x=="O":
            sum=sum+cnt
            cnt=cnt+1
        else :
            sum=sum+cnt
            cnt=0
    sum=sum+cnt
    print(sum)