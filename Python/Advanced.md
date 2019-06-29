## list comprehension
```
res = [x for x in a if x < 3]
res = {x:x for x in a if x < 3}
[do sth data source condition]

product = [(x, y) for x in le if x != 'a' for y in num if y < 3]
```

## generator
gen = (x for x in a if a < 3)
```
next(g) # in python2 is g.next()
```

## crawler
```
import http.client    # python2 is httplib
con = http.client.HTTP(S)Connection('jsonplaceholder.typicode.com')
con.request('GET', '/post')
res = con.getresponse()
data = res.read()
# then data is response content
```

## json
```
import json
parsed = json.loads(data)
parsed...
```

## multi-thread in python
```
# one thread
import httplib
import datetime

def get_data():
    conn = httplib.HTTPSConnection('jsonplaceholder.typicode.com') 
    conn.request('GET', '/posts/1')
    resp = conn.getresponse()
    resp.read()
    
st = datetime.datetime.now()
for i in range(100): 
    get_data()
end = datetime.datetime.now()
print(end - start)

# multi-thread
import http.client
import datetime
import threading

def workder():
    for i in range(100):
        con = http.client.HTTPConnection('jsonplaceholder.typicode.com')
        con.request('GET', '/posts/1')
        res = con.getresponse()
        res.read()
        print('finished')

start = datetime.datetime.now()

threads = []
for i in range(4):
    t = threading.Thread(target=workder())
    threads.append(t)
    t.start()

end = datetime.datetime.now()
print(end - start)

# why not linear impore with multi-thread?
compete resource between thread
```

## queue
```
import queue
import random
import threading
import time

q = queue.Queue() # queue is thread safe in python, int isn't
counter = 0
lock = threading.RLock()


def worker(i, q):
    while True:
        task = q.get()
        print('%d working on task %d' % (i, task))
        time.sleep(1)
        count_new_tasks = random.randrange(0, 10)
        print('putting %d new tasks in queue' % count_new_tasks)
        for new_task in range(count_new_tasks):
            q.put(new_task)

        q.task_done()
        global counter
        with lock:
            counter += 1
            print('processed %d tasks so far' % counter)

for i in range(2):
    t = threading.Thread(target=worker, args=(i, q, ))
    t.setDaemon(False)
    t.start()

q.put(1)
q.join()

```
