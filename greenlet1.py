from greenlet import *

def func1():
    print(1)
    gr2.switch()
    print(11)
    gr2.switch()

def func2():
    print(2)
    gr1.switch()
    print(22)

gr1=greenlet(func1)
gr2=greenlet(func2)

gr1.switch()
