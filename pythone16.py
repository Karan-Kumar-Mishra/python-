#program to find factorial of a number 
num=int(input("Enter the number => "))
i=1
fact=1
while(i!=num):
 fact=fact*i
 i=i+1
print("factorial is => ",fact)