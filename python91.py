class citizen:
    def set_attributes(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
obj1=citizen()
obj1.set_attributes("karan",20)
obj1.display()
obj1.city="lucknow"
print(obj1.name)
print(obj1.age)
print(obj1.city)

