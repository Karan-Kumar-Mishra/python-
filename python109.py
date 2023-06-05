#methode overriding
class citizen:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def display(self):
        print(f"name=>  {self.name}")
        print(f"age=>  {self.age}")
class student:
    def __init__(self,name,age,roll):
        citizen.__init__(self,name,age)
        self.roll=roll
    def display(self):
        print(f"name=>  {self.name}")
        print(f"age=>  {self.age}")
        print(f"roll => {self.roll}")
p1=citizen('rohit',25)
p2=student('ramesh',15,2)
p1.display()
p2.display()
citizen.display(p2)


        
            
        
        