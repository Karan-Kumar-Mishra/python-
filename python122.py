try:
    a=int(input("Enter first number =>"))
    b=int(input("Enter second number =>"))
    c=a/b
    print(c)
    raise
except:
    print("Exception occurred")
print("Program ended after executing statements")
    