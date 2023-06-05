#abstract class
class fruit:
    def cost(self):
        raise NotImplementedError("cost methode is not implemented !")
    def colour(self):
        raise NotImplementedError("colour methode not implemented !")
class apple(fruit):
    def cost(self):
        return "200 rs/kg"
    def colour(self):
        return "red"
class banana(fruit):
    def cost(self):
        return "60 Rs/Dozen"
    def colour(self):
        return "yellow"
    
obj1=apple()
print(f"apple cost :{obj1.cost()}")
print(f"apple cost :{obj1.colour()}")
obj2=banana()
print(f"apple cost :{obj1.cost()}")
print(f"apple cost :{obj1.colour()}")

