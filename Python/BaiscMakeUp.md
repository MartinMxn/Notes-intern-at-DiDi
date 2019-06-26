## python算弱类型语言

####
c=2.5
int(c) # 2

## list可以包含不同类型元素
b[0::2] 隔一个index取一个  
善用负数index b[-1]  
删除 del b[0]  
a[x:y] 到y前一个 

## dict
#### a['name'] and a.get()  
if index doesn't exist, a['name'] will return KeyError  
a.get() return None 

## set
访问index， 转为list  
```
a = [1,2,3]
c = set(a)
list(c)[0]
```
#### set可以取交并差和 
a | b, a & b, a - b, a + b

## format
```
for i in range(10):
  print('number is %d' % i)
```

## input
```
round = input('how many round you want?')
```

## help(你想要看的built-in方法)

## Editors:
pycharm, sublime, atom, vim, emacs

## pip 
dependency management tool of python  
like:  
Java - mvn  
Javascript - npm  

## virtualenv
```
start: virtualenv env  
delete env: rm -r env 
(remove folder)
```
pip freeze > requirements.txt 来生成依赖的版本号  
下一次/其他人开发时候  
pip install -r requirement.txt来安装指定版本依赖

## module
each *.py file is a module
python *.py to execute

## package
A folder has __init__.py inside  
avoid the same name module and ez to manage and import  

## class
```
class Schedule(obj):
    
    name = None
    desp = None
    
    def __inot__(self, n, d):
        self.name = n
        self.desp = d
        
    def __str__(self): # like to string, when print will call this function
        return 'Schedule %s %s' %(self.name, self.desp)
        
    def add_task(self, name, content, priority):
        if name not in self.tasks:
            task = [name, priority, content]
            self.tasks[name] = task
            
    def remove_task(self, name):
        if name in self.task:
            self.task.pop(name, None)
        # pop(k[,d]) If key is not found, d is returned if given, otherwise KeyError is raised
    
    def display(self):
        if self.tasks:
            print('here is your schedule')
            for v in self.tasks.values():
                print('%-10s %-5s %-50s' % (v[0], v[1], v[2])) # indent
    
```

## decorator
add additional function  
In python, function is also first-class object, you may pass function around and use them as arguments for other functions

## read file
```
with open('*.py', 'r') as f:  # with will call __exit()__ at the end automatically
    data = f.read()
    print(data)
# file mode ('r' -> read, 'U', 'w', 'a')  may append(+ for add if file doesn't exist)
```

## command line
```
import sys    # don't forget to import sys

if __name__ == '__main__':
    args = sys.argv
    a1 = args[1]    # command line start with 1, not 0
    a2 = args[2]
```

## Exception
```
try:
    1 + '1'
except TypeError as te:
    print('type are wrong %s' % te.message) # in this case, will only call type error
except Exception as e:
    print('something wrong')
finally:
    print('finally do something')
```
Customized Exception:
```
class AwesomeException(Exception):   # !inherit from Exception
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
# when need throw exception:
raise AwesomeException('message you want to pass for customized exception')
```

## test 
name: test_schedule.py
need pytest dependency
```
def test_add:
    s = Schedule()
    s.add_task('test', 'test test content', 100)
    assert 'test' in s.tasks
    
# and then in the folder run command: pytest
# pytest will auto scan the .py file start with test_*.
# 很多时候会先写test case再写程序去满足
```




