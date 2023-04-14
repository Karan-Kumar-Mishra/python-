#guess number game 
n=18
count=6
while 1:
        
        count=count-1
        print("Number of try => ",count)
        num=int(input("Enter the number =>> "))
        if count==0:
                    print("Game over !!!!")
                    break
        if num>18:
                  print("Enter the less number...")
                  continue
        elif num<18:
                  print("Enter the largest")
                  continue
        elif num==18:
                   print("You get right number")
                   break 
        elif count==5:
                    print("Game over !!!!")
                    break