#Exception
num1=int(input("enter the first number =>"))
num2=int(input("enter the first number =>"))
try:
    print(num1/num2)
except Exception as error:
    print("exception is =>",error)