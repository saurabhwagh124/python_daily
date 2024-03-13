# how to get thread id!
# native thread of PVM is the mainThread itself or just like the mainThread

import threading
print("Start code")
print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
