list1=[1,2,3,4,5,6,7]
list2=[8,9,10,11]
print(list1)
list1.append(8)
print(list1)
list1.extend(list2)
print(list1)
print(list1[::-1])
list1.sort(reverse=True)
print(list1)
list1.insert(2,99)
print(list1)
del list1[2]
print(list1)
list2.pop()
print(list2)
list2.remove(8)
print(list2)
list2.clear()
print(list2)
del list1
print(list1)


