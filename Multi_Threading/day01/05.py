import threading

class MyThread(threading.Thread):
    def __init__(self,x,y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y


    def run(self):
        print("In run method")
        print(threading.current_thread().name)
        print(self.x)
        print(self.y)

print(threading.current_thread().name)
t1 = MyThread(10,20)
t1.start()
