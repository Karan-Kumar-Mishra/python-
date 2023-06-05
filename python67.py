#function
def function():
    print("This is simple function")

function()
#call by reference 
def function2(arg):
    print("call by reference")
    print(arg) 

list1=[1,2,3,4,5,6,7,8]
function2(list1)
#call by value
def function3(data):
    print("call by value")
    data=[1,2,3,4,5] 
    
    print(data)
list1=[1,2,3,4,5,6,7,8]
function3(list1)