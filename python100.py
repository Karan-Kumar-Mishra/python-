#inheritance 
class A:
    a=0
    b=0
    def setdata(self,x,y):
        self.a=x
        self.b=y

class b(A):
    def showdata(self):
        print("a=> ",self.a)
        print("b=> ",self.b)

obj1=b()
obj1.setdata(2,4)
obj1.showdata()
         