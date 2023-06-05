class citizen:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def isVoter(age):
        return age>18
    
obj1=citizen("karan",34)
obj2=citizen("zack",78)
print(citizen.isVoter(obj1.age))
print(citizen.isVoter(obj2.age))


        