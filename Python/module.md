# Module in Python
Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module  
A module is a file containing Python definitions and statements.
####
the module’s name (as a string) is available as the value of the global variable __name__  

#### They are executed only the first time the module name is encountered in an import statement.仅在第一次import时运行
(They are also run if the file is executed as a script.)  

#### Each module has its own private symbol table（私有符号表）
Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.
#### You can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

#### 模块可以引入其他模块，但不一定要放在开头
import all names that a module defines
```
from fibo import *
```
在多数情况下，Python程序员都不会使用这个功能，因为它在解释器中引入了一组未知的名称，而它们很可能会覆盖一些你已经定义过的东西。  


```
如果模块名称之后带有 as，则跟在 as 之后的名称将直接绑定到所导入的模块。

import fibo as fib
fib.fib(500)
```

## Executing modules as scripts
```
python fibo.py <arguments>

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

## 模块搜索路径
当一个名为 spam 的模块被导入的时候，解释器首先寻找具有该名称的内置模块。如果没有找到，然后解释器从 sys.path 变量给出的目录列表里寻找名为 spam.py 的文件。
#### 在初始化后，Python程序可以更改 sys.path。包含正在运行脚本的文件目录被放在搜索路径的开头处， 在标准库路径之前。这意味着将加载此目录里的脚本，而不是标准库中的同名模块。

## “Compiled” Python files
To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc  
eg.: CPython release 3.3 the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc.  
#### 
Python根据编译版本检查源的修改日期，以查看它是否已过期并需要重新编译。这是一个完全自动化的过程。此外，编译的模块与平台无关，因此可以在具有不同体系结构的系统之间共享相同的库。
#### 
Python在两种情况下不会检查缓存。首先，对于从命令行直接载入的模块，它从来都是重新编译并且不存储编译结果；其次，如果没有源模块，它不会检查缓存。为了支持无源文件（仅编译）发行版本， 编译模块必须是在源目录下，并且绝对不能有源模块。

### 
1. The -O switch removes assert statements, the -OO switch removes both assert statements and __doc__ strings. “优化过的”模块有一个 opt- 标签并且通常小些  
2. 一个从 .pyc 文件读出的程序并不会比它从 .py 读出时运行的更快，.pyc 文件唯一快的地方在于载入速度。
3. compileall 模块可以为一个目录下的所有模块创建.pyc文件
4. Reference: <a href="https://www.python.org/dev/peps/pep-3147/">PEP 3147</a>

## 标准模块
一些模块内置于解释器中；它们提供对不属于语言核心但仍然内置的操作的访问，以提高效率或提供对系统调用等操作系统原语的访问。
