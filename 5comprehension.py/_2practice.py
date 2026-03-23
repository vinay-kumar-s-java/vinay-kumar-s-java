#list comprehension
ml=[i**2 for i in range(1,11)]#squares of list  numbers
print(ml)
ml=[i for i in range(1,11) if i%2==0]
print(f"even list {ml}")
w=["Apple","bannana","graphes"]#converting upper case
w=[i.upper() for i in w]
print(w)
#create new list greather than 10
populationlist=[10,11,25,67,43,24,8,5]
populationlist=[i for i in populationlist if(i>10)]
print(f"population greather than 10:{populationlist}")
L=[]
for i in range(1,11):
    if(i%2==0):
        L.append("even")
    else:
        L.append("odd")
print(L)