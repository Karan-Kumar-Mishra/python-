#locals
def locals_demo(x,y):
    s='foo'
    z=x+y
    print('the sum=> ',z)
    print('the dictionary for namespace is')
    print(locals())
locals_demo(2,5)
#

def karan():
    print("simple")
    s="kkm"
    print(locals())
print()
print()
print()

karan()
#globals
print(globals())  