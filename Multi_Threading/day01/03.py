# creating multiple threads and their functionality check

import threading

def fun():
    print("In fun function")
    print(threading.current_thread().name)
    for i in range(6):
        print("In Fun")

def mun():
    print("In mun function")
    print(threading.current_thread().name)
    for i in range(6):
        print("In Mun")

print(threading.current_thread().name)

thread1 = threading.Thread(target = fun)
thread2 = threading.Thread(target = mun)

thread1.start()
thread2.start()
