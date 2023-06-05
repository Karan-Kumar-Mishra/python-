#lamda  or anonymous function
def sum(a,b):
    print("simple function=>",a+b)

sum(2,2)
sum= lambda x,y: print("lamada function =>",x+y)
sum(2,2)

sub= lambda x,y: x-y
# sub= lambda x,y: return x-y              error

print(sub(4,2))

def inc(y):
    return(lambda x:x+1)(y)

print(inc(10))