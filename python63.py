def function():
    print("karan kumar mishra")
func2=function
func2() 

def funcret(num):
    if num==0:
        return print
    if num==1:
        return int
a=funcret(0)
print(a)

print(print)

def executor(func):
    func("this")
executor(print)

def decl(func1):
    def nowexe():
        print("Executing now")
        func1()
        print("Executed")
    return nowexe

def who_is_zack():
    print("zack is good boy")

who_is_zack()