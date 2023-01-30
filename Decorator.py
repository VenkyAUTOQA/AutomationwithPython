from datetime import datetime as dt
import time

def Decorator(func):
    def inner():

        print(dt.now())
        func()
        # time.sleep(5)
        print(dt.now())
    return inner
def decor():
    print('I am decorated')

dec= Decorator(decor)
dec()