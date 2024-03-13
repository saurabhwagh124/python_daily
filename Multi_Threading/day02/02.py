# creating thread using thread class as parent class 

import threading
from threading import Thread

class MyThread(Thread):
    def run(self):
        print("In run")
        print(threading.current_thread().name)

print("Main Thread Start")
t1 = MyThread()
t1.start()
print("Main Thread End")
