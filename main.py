import _thread
import logging
import threading
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)

loops = [2,4]

def loop(nloop,nses):
    logging.info("start" + str(nloop) + "at" + ctime())
    sleep(nses)
    logging.info("end" + str(nloop) + "at" + ctime())

class myThread(threading.Thread):
    def __init__(self,func,args,name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def main():
    logging.info("start all at" + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = myThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())
# def loop0():
#     logging.info("start loop0 at" + ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at" + ctime())

# def main():
#     logging.info("start all at" + ctime())
#     loop0()
#     loop1()
#     logging.info("end all at" + ctime())

# def main():
#     logging.info("start all at" + ctime())
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1, ())
#     sleep(6)
#     logging.info("end all at" + ctime())

# def main():
#     logging.info("start all at" + ctime())
#     locks = []
#     nloops = range(len(loops))
#     for i in nloops:
#         lock = _thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#     for i in nloops:
#         _thread.start_new_thread(loop,(i,loops[i],locks[i]))
#     for i in nloops:
#         while locks[i].locked():pass
#     logging.info("end all at" + ctime())


if __name__ == "__main__":
    main()