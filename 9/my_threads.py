import threading
from time import sleep, ctime


def payload(thread_name, interval):
    for r in range(10, 0, -1):
        print(f"{ctime()} - {thread_name} - {r}\n")
        sleep(interval)


t1 = threading.Thread(target=payload, args=('first', 1))
t2 = threading.Thread(target=payload, args=('second', 1))

t1.daemon
t1.start()

t2.daemon
t2.start()
