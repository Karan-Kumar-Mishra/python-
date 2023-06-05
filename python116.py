import json
data='{"var1":"harry","var2":56}'
#print(prsed['var1']) error
prsed=json.loads(data)
print(prsed)
print(prsed['var1'])
print(type(prsed))