def sq(a):
    return a*a
num=[2,3,5,6,7,8,9]
square=list(map(sq,num))
print(square) 

square=list(map(lambda x: x*x,num))
print(square) 

list_1=[1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5
gr_than_5=list(filter(is_greater_5,list_1))
print(gr_than_5)