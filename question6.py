#function argument in python
# Required argument 
def function1(k):
    print(k)

#function1() error
#Keyword argument 
def function2(str):
    print(str)
function2("keyword")
#default argument
def function3(k="karan"):
    print(k)
function3("mishra")
#Variable length argument 
def function4(*k):
    for i in k:
        print(i)
function4("karan","kumar","mishra ")

