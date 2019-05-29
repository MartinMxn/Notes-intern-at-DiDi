# PythonCrashCourse

# List
## Insert
使用方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
```
motorcycles.insert(0, 'ducati')
```

## Delete
```
del motorcycles[0]
```

## Pop
```
popped_motorcycle = motorcycles.pop()
```

## Find and Delete
```
motorcycles.remove('ducati')

#If not exist:
ValueError: list.remove(x): x not in list
```

## Sort

### Foever sort
```
sort()
你还可以按与字母顺序相反的顺序排列列表元素，为此，只需
cars.sort(reverse=True)
```

### tmporary sort
```
print(sorted(cars))
```

### Reverse/Len
reverse()
len()
#### 索引-1 总是返回最后一个列表元素

### Traverse
```
for magician in magicians:
```

#### Indent error
Python根据缩进来判断代码行与前一个代码行的关系
对于位于for 语句后面且属于循环组成部分的代码行，一定要缩进
```
for magician in magicians:
print(magician.title() + ", that was a great trick!")
❶ print("I can't wait to see your next trick, " + magician.title() + ".\n")
```
**!!由于变量magician 的终值为'carolina'**

#### Colon error 

### range()
```
for value in range(1,5):
print(value)
```
函数range() 让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。  
**使用函数range() 时，还可指定步长**
even_numbers = list(range(2,11,2))

### list()
要将这些数字转换为一个列表，可使用list()
```
numbers = list(range(1,6))
```

### Number function:
min(digits)
max(digits)
sum(digits)

### List comprehension
```
squares = [value**2 for value in range(1,11)]
```
列表解析 将for 循环和创建新元素的代码合并成一行，并自动附加新元素。
**这里的for 语句末尾没有冒号。**

### Slice
可指定要使用的第一个元素和最后一个元素的索引。
```
print(players[0:3])
# 这将输出分别为0 、1 和2 的元素。

# 如果你没有指定第一个索引，Python将自动从列表开头开始：
print(players[:4])

要让切片终止于列表末尾，也可使用类似的语法。
print(players[2:])

负数索引返回离列表末尾相应距离的元素，因此可以输出列表末尾的任何切片。
例如，如果你要输出名单上的最后三名队员
players[-3:] ：

要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引
[:] 
friend_foods = my_foods[:]
```
