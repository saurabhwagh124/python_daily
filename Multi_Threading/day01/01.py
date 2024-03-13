# visit cd usr/lib/python version/threading.py to get an insight of the python library

#Method 1 of creating thread i.e. Creating thread using import threading

import threading

print("Start code")

def fun():
    print("In Fun")
print(threading.current_thread().name)
threading.current_thread().name = "SaurabhWagh"
fun()

print(threading.current_thread().name)


