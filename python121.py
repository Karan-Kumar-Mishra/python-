a=int(input("Enter the first number =>"))
b=int(input("Enter the first number =>"))
try:
  c=a/b
except ZeroDivisionError:
    print("error")
else:
    print("else block")


