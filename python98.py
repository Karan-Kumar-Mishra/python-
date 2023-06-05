#Iterator
def gen(n):
    for i in range(n):
        yield i

g=gen(4)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

k="karan"
itr=iter(k)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())



         