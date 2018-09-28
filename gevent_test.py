import gevent
import time

def foo(a,b):
    print('a=%d,b=%d'%(a,b))
    gevent.sleep(2)
    print('Running foo again')

def bar():
    print('Running into bar')
    gevent.sleep(3)
    print('Running bar again')

# 生成协程
f=gevent.spawn(foo,1,2)
g=gevent.spawn(bar)
# time.sleep(3)
print('=======')
gevent.joinall([f,g])
