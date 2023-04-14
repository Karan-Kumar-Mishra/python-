
import time
'''
initial=time.time()
for i in range(50):
                   print("for loop")
                   print(time.time() -initial,"second")
i=1
while(i<=50):
             print("while")
             i=i+1
             print(time.time() -initial,"second")
 '''
while(1):
         localtime=time.asctime(time.localtime(time.time()))
         print(localtime)
         time.sleep(1)