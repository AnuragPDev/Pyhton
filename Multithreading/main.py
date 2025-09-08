from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
        
            print("hello")
            sleep(1)

class Hii(Thread):
    
    def run(self):
        for i in range(5):
            print("Hiii")
            sleep(1)

t1=Hello()
t2=Hii()

t1.start()
t2.start()
t1.join() # main thread will wait for join the two threads
t2.join()
print("bye")