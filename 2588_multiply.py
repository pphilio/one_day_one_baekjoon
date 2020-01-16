a=int(input())
b=int(input())
i=0
sum=0
arr1=[]
while(b>0):
    arr1.append(b%10)
    b=int(b/10)
    i=i+1
i=1
for num in arr1:
    print(num*a)
    sum=sum+num*a*i
    i*=10
print(sum)