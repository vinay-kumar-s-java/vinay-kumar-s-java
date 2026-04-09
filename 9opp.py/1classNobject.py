class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name={self.name}\nage={self.age} ")
std1=Student(age=19,name="vinay")
std1.display()
class rectangle:
    def __init__(self,len,brdth):
        self.length=len
        self.breadth=brdth
    def display(self):
        return self.length*self.breadth
    
a1=rectangle(10,20)
print(a1.display())