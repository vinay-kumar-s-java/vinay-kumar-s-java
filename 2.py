list=[200,10,20,100,200,199,30,40,50]
firlargest=list[0]
seclargest=list[1]
for i in list:
    if(i>firlargest ):
            seclargest=firlargest
            firlargest=i
    if(i>seclargest and  i<firlargest):
            seclargest=i

print(f"first lar {firlargest} sec lar{seclargest}")
