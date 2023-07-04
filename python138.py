import threading
import time
def function1():
    print("This is simple function 1")
    time.sleep(2)
    print("funtion1 done ")
def function2():
    print("This is simple function 2")
    time.sleep(2)
    print("funtion2 done ")
    
    
if __name__=="__main__":
    thread1=threading.Thread(target=function1)
    thread2=threading.Thread(target=function2)
    thread1.start()
    thread2.start()
    
    
    