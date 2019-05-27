# Hello World
```
print("Hello Py world!")
```
在Python 2代码中，有些print语句包含括号，有些不包含。  
####

# Variables
```
message = "Hello Py world!"
print(message)
```
变量名只能包含字母、数字和下划线。不能以数字打头  
变量名不能包含空格  
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0  
就目前而言，应使用小写的Python变量名  

## String
在Python中，用引号括起的都是字符串，可以是单引号，也可以是双引号  
```
name = "ada lovelace"
print(name.title())

Ada Lovelace
```
title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。  
name = "Ada Lovelace" 
print(name.upper()) 
print(name.lower())
存储数据时，方法lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为 最合适的大小写方式。  

### concate string '+'
```
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

Hello, Ada Lovelace!
```

### carriage returns/tab characters/space
要在字符串中添加制表符，可使用字符组合\t :
```
>>> print("Python")
Python
>>> print("\tPython")
Python
```
要在字符串中添加换行符，可使用字符组合\n :
```
>>> print("Languages:\nPython\nC\nJavaScript") Languages:
Python
C
JavaScript
```

#### clear space
删除末尾空白rstrip()。 
lstrip() => left  
strip() => both

### syntax error
```
message = "One of Python's strengths is its diverse community."
print(message)
```
✅
```
message = 'One of Python's strengths is its diverse community.'  # single quote
print(message)
```
❎

## Number
+,-,*,/, **(power) 
### Float
Python将带小数点的数字都称为**浮点数**  
但需要注意的是，结果包含的小数位数可能是不确定的:  
```
>>> 0.2 + 0.1 0.30000000000000004 
>>> 3 * 0.1 0.30000000000000004
```

### str() * => string

### integer in python2
**python2**
```
>>> 3 / 2
1
```
计算整数结果时，采取的方式不是四舍五入，而是将小数部分直 接删除。  
**python3**
```
>>> 3 / 2
1.5
```
在Python 2中，若要避免这种情况，务必确保至少有一个操作数为浮点数，这样结果也将为浮点数

## comments
single line by '#'
multiple line by ''' ''' or """ """

## import this => show the zen of python...
