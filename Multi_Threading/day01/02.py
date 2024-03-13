# getting process id of  a thread
import threading, os

for x in range(11):
    print(x)

print(threading.current_thread().name)
print(os.getpid())
