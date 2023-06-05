#desconstructor 
class temp:
    def __del__(self):
        print("desconstructor is called")

obj1=temp()
