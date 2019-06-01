## loop

### For
```
循环语句可能带有一个 else 子句；它会在循环遍历完列表 (使用 for) 或是在条件变为假 (使用 while) 的时候被执行，但是不会在循环被 break 语句终止时被执行。 这可以通过以下搜索素数的循环为例来进行说明:

>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

### 关键字参数 end 可以用来取消输出后面的换行, 或是用另外一个字符串来结尾:
```
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',') # end in print
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

### 如果在循环内需要修改序列中的值（比如重复某些选中的元素）   
可以先拷贝一份副本。对序列进行循环不代表制作了一个副本进行操作。切片操作使这件事非常简单：
```
words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
```

### range
```
>>> for i in range(5):
...     print(i)

>>> print(range(10))
range(0, 10)
```

### pass
什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它。例如:
```
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...

pass 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，允许你保持在更抽象的层次上进行思考。 pass 会被静默地忽略:
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```

## Function
关键字 def 引入一个函数 定义。它必须后跟函数名称和带括号的形式参数列表。
构成函数体的语句从下一行开始，并且必须缩进。
#### 

在函数被调用时，实际参数（实参）会被引入被调用函数的本地符号表（local symbol table）中
因此，实参是通过**按值调用**(传递对象的**引用**而不是对象的值）。
#### 

即使没有 return 语句的函数也会返回一个None值(内置名称)  

**重要警告:**  
默认值只会执行一次。
```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

[1]
[1, 2]
[1, 2, 3]
```
如果你不想要在后续调用之间共享默认值, 可以:
```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
####
可变参数 *args  
字典可以使用 ** 运算符来提供关键字参数
####
解包参数列表 ？
```
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```


### in (key word)
```
in 和 not in 用于成员检测

对于字符串和字节串类型来说
一个等价的检测是 y.find(x) != -1
```
