#set
set1={1,2,3,4,5,6,7,8,9}
print(type(set1))
print("set1=> ",set1)
set2=set(['a','b','c','d'])
set3={1,2,'a',"karan",34.7}
set4=set('welcome')
set5=set((1,2,3,4,5))
print("set2=>",set2)
print(set3)
print(set4)
print(set5)
set6={'hi','my','name','is','karan'}
print('hi' in set6)
set7={10,20,30,40,50,60}
set7.add(70)
print("add=> ",set7)
set7.update(set1)
print("upadte=> ",set7)
set7.remove(70)
print("remove=> ",set7)
set7.discard(2)
print("remove=> ",set7)
set7.pop()
print("pop =>",set7)
print("copy=> ",set7.copy())
print("union =>",set7.union(set1))
print("difference => ",set7.difference(set1))
print("intersection=> ",set7.intersection(set1))
print("difference_update => ",set7.difference_update(set1))
print("isdisjoint=> ",set7.isdisjoint(set1))
print("issubset=> ",set7.issubset(set1))
print("issuperset=> ",set7.issuperset(set1))
print("symmetric_difference=> ",set7.symmetric_difference(set1))
print("symmetric_difference_update=> ",set7.symmetric_difference_update(set1))
print("intersection_update=> ",set7.intersection_update(set5))
print("symmetric_difference_update=> ",set7.symmetric_difference_update(set5))





