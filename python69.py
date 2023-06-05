#Global variable
var=10
def function():
    print(var)
function()

#local variable
def function2():
    var=20
    print(var)
function2()

#global keywords
a=10
def temp1():
    a=45
    print(a)
temp1()


b=10
def temp2():
    global b
    print(b)
temp1()