# find sum of digits of a number
num=int(input("Enter the number =>"))
while (num>0):
        print(int(num%10),end=' ')
        num=int(num/10)
