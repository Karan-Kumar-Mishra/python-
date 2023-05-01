# dictionary
dict1={1:'one',2:'two',3:'three'}
print("dict1=> ",dict1)
dict2={'one':"ONE",'two':"TWO",'three':"Three"}
print("dict2=> ",dict2)
dict3={1:"one",2:"two",3:"three",'nested':{1:"red",2:"green",3:"black"}}
print("dict3=>",dict3)
dict4={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six'}
print("dict4=> ",dict4)
print("dict4.pop=> ", dict4.pop(1))
print("dict4.popitem=> ", dict4.popitem())
print("dict4.copy=> ", dict4.copy())
dict4.update(dict1)
print("dict4.update=> ",dict4)
#print("dict4.str=> ",dict4.str())
print("dict4.keys=> ",dict4.keys())
print("dict4.items=> ",dict4.items())
#print("dict2.cmp=> ",dict4.cmp(dict1))
print('dict4.has_key(2)=> ',2 in dict4)




