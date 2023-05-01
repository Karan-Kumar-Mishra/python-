#queue implimention using list
queue=[]
def enqueue(data):
    queue.append(data)
def dequeue():
    del queue[0]
def display():
    print(queue)
 
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
display()
dequeue()
dequeue()
display()

   