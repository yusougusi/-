from time import time, localtime, sleep



class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
            (self._hour, self._minute, self._second)


def main():
    time = Time.now()
    while True:
        print(time.show())
        sleep(1)
        time.run()



if __name__ == '__main__':
    main()
