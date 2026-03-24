for i in range(1,11):
    print(i,end=" ")#printing 1 to 10
print()
#sum of n numbers
n=5
sum=0
for i in range(n+1):
    sum+=i
print("sum of n numbers"+str(sum))   
#check if a no is even or odd
a=10
if(a%2==0):
    print('Even')
else:
    print("odd")
#largest of three no
lis=[10,20,30,787,1,2]
max=lis[0]
i=1
for i in range(len(lis)):
    if(lis[i]>max):
        max=lis[i]

print("maximun is"+str(max))
#reverse a number
num=123
rev=0
while num>0:
    n=num%10
    rev=rev*10+n
    num=num//10
print(rev)
print(1//10)
print(1%10)

