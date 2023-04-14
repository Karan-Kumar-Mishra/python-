# Function 
def function1():
                """This is simple function"""
                print("This is function1")
      
function1()

print("doc =>",function1.__doc__)
def add(num1,num2):
                   print("a+b=> ",num1+num2)
add(3,2)

def sub(num1,num2):
                   return num1-num2
print("a-b=> ",sub(5,2))

def multi():
            a=2
            b=4
            return a*b
print("a*b=> ",multi())