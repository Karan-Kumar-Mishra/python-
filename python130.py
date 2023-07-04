#OS module
import os
crd=os.getcwd()
print("current directory :",crd)
os.chdir(r"C:\Users\91888\Documents")
crd=os.getcwd()
print("current directory :",crd)
os.mkdir(r"C:\Users\91888\Documents",0755)
os.makedirs("C:\Users\91888\Documents\python")