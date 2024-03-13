# 3rd method to create thread 

import threading
class Demo():
    def dispInfo(self):
        print("In dispInfo")
        print(threading.current_thread().name)
        print(t1.name)

    def dispData(self):
        print("In DispData")
        print(threading.current_thread().name)
        print(t2.name)

print("Main Threadd")
obj = Demo()
t1 = threading.Thread(target = obj.dispInfo)
t2 = threading.Thread(target = obj.dispData)

t1.name = "Saurabh Wagh"
t2.name = "Saurabh Wagh2"
t1.start()
t2.start()
print("End")
