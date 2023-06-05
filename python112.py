class ComplexNum:
    def __init__(self,r,i):
        self.real= r 
        self.imag= i 
    def __str__(self):
        imag=self.imag
        join='+'
        if(imag<0):
            imag=-imag
            join='-'
        self.s='str'
        return '(' + str(self.real)+join +'j'+str(imag)+')'
    def __add__(self,oth):
        return ComplexNum(self.real+oth.real,self.imag+oth.imag)
z1=ComplexNum(2,3)
print('z1= ',z1)
z2=ComplexNum(4,2)
print('z2= ',z2)
z3=z2+z1
print(f"z1+z2={z3}")        