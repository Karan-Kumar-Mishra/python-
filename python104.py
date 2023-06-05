ls=[]
for i in range(10):
    if i%3==0:
        ls.append(i)
print(ls)
ls=[i for i in range(100) if i%3==0]
print(ls)
dicit={i:f"item{i}" for i in range(100)}
print(dicit) 
dict2={i:f"item {i}" for i in range(5)}
print(dict2)
dresses={
    dress for dress in [ "dress1","dress1","dress1","dress1","dress1"]    }
evens=(i for i in range(100) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
