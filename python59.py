#stack implimention using list
stack=[]
def push(data):
    stack.append(data)
def display():
    print(stack)
def pop():
    stack.pop()
def peek():
    return stack[0]
push(10)
push(20)
push(30)
push(40)
display()
pop()
display()
print(peek())
