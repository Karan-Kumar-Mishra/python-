class employee:
    def __init__ (self,name,salary):
        self.name=name 
        self.salary=salary
    @classmethod
    def salary(cls,name,salary):
        return cls(name,salary)
obj1=employee("karan",12)
obj2=employee("mishra",13)
print(obj1.salary)
print(obj2.salary)


    