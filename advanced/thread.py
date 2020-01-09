import threading
import time


class Timer(threading.Thread):

    def __init__(self, name, sleep, count):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep = sleep
        self.count = count
        self.runner = False
        # self.daemon = True # enabled action daemon

    def run(self):
        self.runner = True
        while True:
            if self.count == 0:
                print("End Timer", self.name)
                break
            day = time.localtime()
            if self.runner:
                print(self.name, day.tm_hour, ":", day.tm_min, ":", day.tm_sec)
                self.count -= 1
                time.sleep(self.sleep)

    def stop(self):
        self.count = 0

    def pause(self):
        self.runner = False

    def continues(self):
        self.runner = True

    def is_run(self):
        return self.runner


timer = Timer("Timer 1: ", 2, 50)

timer.start()
time.sleep(10)
if timer.is_run():
    timer.pause()
time.sleep(10)
if not timer.is_run():
    timer.continues()
time.sleep(5)
timer.stop()


############
def service():
    print
    threading.currentThread().getName()


t = threading.Thread(target=service, name='Service')
# t.setDaemon(True) # enabled action daemon
t.start()
