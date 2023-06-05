#static method
class temp:
     @staticmethod
     def function():
         var="This is static method"
         print(var)
     def function2(self):
        print("This is not static methode")
 
obj1=temp()
obj2=temp()
obj3=temp()
obj1.function()
obj1.function2()
obj2.function()
obj2.function2()
obj3.function()
obj3.function2()

temp.function()

       