#Exception
num1=int(input("enter the first number =>"))
num2=int(input("enter the first number =>"))
try:
    print(num1/num2)
except ZeroDivisionError as error:
    print("exception is =>",error)
except ValueError as error:
    print("exception is =>",error)
except Exception as error:
    print("exception is =>",error)