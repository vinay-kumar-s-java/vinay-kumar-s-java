def reverseNO(num):
    while(num!=0):
        a=num%10
        #b=a*10+a
        num=num//10
    return a
print(reverseNO(50))

