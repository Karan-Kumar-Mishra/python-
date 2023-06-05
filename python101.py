#multiple inheritance
class A:
    a=0
    b=0
    def setdata(self,x,y):
        self.a=x
        self.b=y
class B:
    def showdata(self):
        print("a=> ",self.a)
        print("b=> ",self.b)

class C(A,B):
    def function(self,x,y):
        self.setdata(x,y)
        self.showdata()
obj1=C()
obj1.function(2,8)
        
        
        