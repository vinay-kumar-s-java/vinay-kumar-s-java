class player:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
            print(f"name={self.name}\nage={self.age}")
a1=player("Virat",37)
a2=player("rohit",37)
a1.display()


        