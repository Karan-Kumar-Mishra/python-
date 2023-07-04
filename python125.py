#Built-in Exception
class myException(Exception):
    def function(self):
        ex=myException()
        raise ex

obj1=myException()
obj1.function()    