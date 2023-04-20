from datetime import datetime
from time import localtime
from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            logit_string = f"{func.__name__} was called at {datetime.now()}"
            print(logit_string)
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(logit_string + '\n')
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        pass


@logit()
def myfunc1():
    pass


myfunc1()
