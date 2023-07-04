class myException(Exception):
    def function(self):
        raise myException

obj=myException()
obj.function()