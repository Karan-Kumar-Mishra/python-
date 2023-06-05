class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email= f"{fname}.{lname}@zack.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"
    def printemail(self):
        pass
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@zack.com"
    @email.setter
    def email(self,string):
        names=string.split("%")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
        
    
kkm=employee("karan","mishra")
print(kkm.email())
kkm.fname="jack"
print(kkm.email)
#pending 