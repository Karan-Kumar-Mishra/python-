class myException(Exception):
    def function(self):
        try:
            ex=myException()
            raise ex
        except Exception as e:
            print(e)
            print("Exception is sucessfully manage !")

obj1=myException()
obj1.function()
    