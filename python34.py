# 
def function(n,*s,**m):
                       print(n)
                       for iteam in s:
                                      print(iteam)
                       for key ,value in m.items():
                                                   print(key,value)

l=["karan","kumar","mishra"]
normal="This is normal string"
k=["zack","mishar"]
function(normal,*l,k)
 