import threading
from threading import Thread

print(type(threading.current_thread()))

t1 = Thread()
print(type(t1))
