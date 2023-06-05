# Access specifirs
class temp:
    var =89 #public access specifirs
    __age=10 # private access specifirs
obj1=temp()
print(obj1.var)

#print(obj1.__age) error
print(obj1._temp__age)

    