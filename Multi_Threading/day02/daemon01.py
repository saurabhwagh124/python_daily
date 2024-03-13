import threading
import time
from threading import Thread
class Demo():
    def fun(self):
        time.sleep(8)
        print("In fun")
        print(threading.current_thread().name)

    def gun(self):
        time.sleep(1.10)
        print("In gun")
        print(threading.current_thread().name)

print("Main Thread")
obj = Demo()
t1 = Thread(target = obj.fun,daemon = True)
t2 = Thread(target = obj.gun)
t1.start()
t2.start()
print("End Main")
