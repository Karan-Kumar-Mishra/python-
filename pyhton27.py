# find the factorial using recursion
def function(fact):
                  if(fact==1):
                              return 1;
                  
                  return fact*function(fact-1);
                  
print("Factorial =>",function(int(input("Enter any number=> "))))