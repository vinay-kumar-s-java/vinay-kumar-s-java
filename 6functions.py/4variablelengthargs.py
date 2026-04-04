#key word arguments(takes as dictionary)
def demo(**a):
   a=a.items()
   for key,value in a:
      print(f"{key} {value}",end=" ")
   print() 
    
   
demo(rama="sita",krishna="radha",narayana="lakshmi")
#arguments
def display(*a):
   return sum(a)
print(display(12,34,53))

