try:
    num1=input("enter the first number =>")
    num2=input("enter the first number =>")
    c=num1/num2   
except(ZeroDivisionError,KeyboardInterrupt,ValueError,TypeError):
    print("error")
