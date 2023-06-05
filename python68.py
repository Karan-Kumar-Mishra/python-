#function arguments

#keyword Arguments
def function1(int):
    print(int)
function1("This is a simple function ....")

#default Arguments
def function2(a=10,b=20,c=30):
    print("a=>",a)
    print("b=>",b)
    print("c=>",c)
function2(1)
function2(1,2)
function2(1,2,3)

#Variable-length Arguments
def function3(a,*arg):
    print(a)
    for i in arg:
        print(i)
function3(10)
function3(10,56,78,90)

#Required Arguments
def function4(num):
    print(num)
function4()

    