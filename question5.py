#deffrence between call by value and call by reference 
#1 Call by value 
def function(list1):
    list1=[1,2,3,4]
    print("Call by value In side of function => ",list1)
    

list1=[10,20,30,40]
function(list1)
print("Call by value Out side of function => ",list1)

#2 Call by reference
 
def function(list1):
    list1.append([1,2,3,4])
    print("Call by reference In side of function => ",list1)
    

list1=[10,20,30,40]
function(list1)
print("Call by reference Out side of function => ",list1)
