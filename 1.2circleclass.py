class circle:
    def __init__(self,radius):
        self.radius=radius
    def display(self):
        return self.radius*self.radius
a=circle(10)
print(type(a))
        