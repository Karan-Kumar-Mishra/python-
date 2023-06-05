#operator overloading
class temp:
    a=0
    b=0
    def setdata(self,x,y):
        self.a=x
        self.b=y
    def showdata(self):
        print("a=> ",self.a)
        print("a=> ",self.a)
    def __add__(self,other):
        tp=temp()
        tp.a=self.a+other.a
        tp.b=self.b+other.b
        return tp
    
obj1=temp()
obj2=temp()
obj1.setdata(2,4)
obj1.setdata(6,8)
print((obj1+obj2).a)
print((obj1+obj2).b)        
        
        
        
                