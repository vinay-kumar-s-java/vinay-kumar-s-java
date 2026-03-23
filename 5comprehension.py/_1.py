#comprehension
my_list=[0,1,2,3,4,5,6,7,8,9]
for x in my_list:
    if(x%2):
        print(x)
city_population={
    "bengaluru":84,
    "Mysuru":11,
    "Kannakapura":12,
    "mandya":7
}
large_city={key:value for key,value in city_population.items() if(value>=10)}

print(large_city)

ml=[]
for i in range(0,10):
    n=input("Enter the numbers to list")
    ml.append(n)
  
print(ml)
#string split
name="Vinay Kumar basya"
nl=name.split(" ")
print(nl)

mylist=["1","2","3"]
a=0
il=[]
for i in mylist:
    a=int(i)
    il.append(a)
    
