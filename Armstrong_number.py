number=input("Enter the number =>")
temp=int(number)
m=len(number)
sum=0
while(int(number)>0):
    r=int(number)%10
    sum=sum+pow(r,m)
    number=int(number)/10
if(temp==sum):
    print("Armstrong number")
else:
    print("Not Armstrong number")
    
    