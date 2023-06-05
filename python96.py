#static method
class temp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def isVoter(age):
        return age>18
    
ob1=temp("karan",25)
ob2=temp("karan",12)

print(temp.isVoter(ob1.age))
print(temp.isVoter(ob1.age))
