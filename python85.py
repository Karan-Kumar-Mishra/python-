#program to  demonstrate numpy ,pandas, and Scipy
#packeges in one program
import numpy
import pandas as pd
from scipy import constants
l=[12.34,45.56,68.78,98.78]
a=numpy.array(l)
print("Temp in c are ",a)
f=(a*9/5+32)
print("the temp in 'f' are:",f)
print(constants.pi)
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)
myvar=pd.Series(a,index=['x','y','z'])
print(myvar)




