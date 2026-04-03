"""def check(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
print(check(23))
def largestofThreeno(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"the largest no is {num1}")
    elif(num2>num1 and num2>num3):
        print(f"the largest no is {num2}")
    elif(num3>num2 and num3>num1):
        print(f"the largest no is {num3}")
largestofThreeno(5,6,4)"""
def countEvenno(list):
    count=0
    for i in list:
        if(i%2==0):
            count=count+1
    return count
lis=[0,2,4]
noOfEven=countEvenno(lis)
print(noOfEven)


