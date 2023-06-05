import pickle
cars=["Audi","BMW","MARUTI SUZUKI"]
file="mrzack.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()
#print(cars)
file="mrzack.pkl"
fileobj2=open(file,'rb')
mycar=pickle.load(fileobj2)
print(mycar)