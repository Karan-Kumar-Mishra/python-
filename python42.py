#find max number is in three number 
num1=int(input("Enter the fist number =>"))
num2=int(input("Enter the second number =>"))
num3=int(input("Enter the three number =>"))
if num1>num2:
    if num1> num3:
        print("max=> ",num1)
    else:
        print("max=> ",num3)
elif num2>num1:
    if num2>num3:
        print("max=> ",num2)
    else:
        print("max=> ",num3)
elif num3>num1:
    if num3>num2:
        print("max=> ",num3)
    else:
        print("max=> ",num2)
        
        
        
        