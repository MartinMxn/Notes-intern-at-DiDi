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
import queue     # python is Queue

q = queue.Queue()
for i in range(100):
    q.put(i)

while not q.empty():
    print(q.get())

```
