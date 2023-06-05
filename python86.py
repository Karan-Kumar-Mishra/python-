from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
    
class reactangle(shape):
     type="Reactangle"
     side=4
     def __init__(self):
         self.length=6
         self.breadth=7
     def printarea(self):
         return self.length * self.breadth
obj=reactangle();
print(obj.printarea())
