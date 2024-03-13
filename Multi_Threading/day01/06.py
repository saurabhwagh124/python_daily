import threading
class MyThread():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def disp(self):
        print("In display")
        print(self.x)
        print(self.y)
        print(threading.current_thread().name)

print(threading.current_thread().name)
obj = MyThread(10,110)
t1 = threading.Thread(target = obj.disp)
t1.start()
