#input of n no perform less than n square roots
if __name__ == '__main__':
    n = int(input())
    lis=[]
    for i in range(n):
        lis.append(i)
    for i in lis:
        print(i*i)  
