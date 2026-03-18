#input() it takes input from user from keybord
name=input("Enter your name:")
age=int(input("Enter your age:"))
if(age>=18):
    print("your adult")#print functiom is display the output the text variabbles or result of expression:

#String manipulation
first_name="Vinay"
second_name="Kumar"
full_name=first_name+" "+second_name#concate of 3 strings
print(full_name)
#string repition
message=("warning"+" ")*3
print(message)#output =warning warning warning"""

#string method
my_string="Hello     "
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
a=my_string.replace("l","w")
print(a)
#slicing
print(my_string[::2])#Start Step Stop