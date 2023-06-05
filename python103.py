#multipath inheritance

class A:
    a=0
    b=0
    
class B(A):
    def setdata(self,x,y):
        self.a=x
        self.b=y
class C(A):
    def showdata(self):
        print("a=> ",self.a)
        print("b=> ",self.b)
class D(B,C):
    def display(self,x,y):
        self.setdata(x,y)
        self.showdata()

obj1=D()
obj1.setdata(2,8)
obj1.showdata()
obj1.display(4,5)        
        
        