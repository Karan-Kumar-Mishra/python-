#find the factorial of ginven number
num=int(input("Enter the number => "))
fact=1
for i in range(1,num):
    fact=int(fact*i)
print("factorial is =>",fact)