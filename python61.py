#implimention of queue using collection deque
from collections import deque
queue=deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
