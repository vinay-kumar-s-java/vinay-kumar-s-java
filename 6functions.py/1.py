def greet():
    print("Gagan "*3)
    return "Gagan "*3
print(greet())#first greet function prints print()(inside of greet()) second prints return type of function

#parameters are variables to pass data to function
def add(num1,num2):
    return num1+num2
sum=add(32,34)
print(sum)
#default value(it is requiered no argument pass)
def marriage(boy,girl="girl"):
    print(f"{boy} marry {girl}")

marriage("Vinay","Vinaya")