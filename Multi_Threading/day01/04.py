# Creating thread using 2nd method

from threading import Thread
import threading

class MyThread(Thread):
    def run(self):
        print(threading.current_thread().name)
        print(threading.current_thread().is_alive())
        #threading.current_thread()._stop()
        # is related to some lock or something
        print(threading.current_thread().is_alive())

        print(threading.current_thread().is_alive())

print(threading.current_thread().name)
t1 = MyThread()
t1.start()
