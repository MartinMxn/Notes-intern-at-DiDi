# Note for You don't know JS I (of III)

# Part 1

## Chapter one  

### Into programming  
#### Shortcut:  
chrome console: command + option + J  
chrome Elements: command + option + I  
#### Input:  
prompt('message you want to show:')  

####  

Compund operators: +=, -=, *=, /= ...  

####  

'Convert' operation in JS called 'coercion'  

####  

Some methods to forcibly coercing between types:  
String -> Number  
let a = '42';  
let b = Number(a);

####  

Naming for constants with underscore _ , ie: TAX_RATE = 0.08
Block {} doesn't need ;

####  

When use == loose-equals operator to make comparsion '99.99' == 99.99, JS will convert the left-hand side to its number 99.99

####  

#### Scope(lexical scope):  
Scopeis basically a collection of variables as well as the rules for how those variables are accessed by name.  
variable name has to be unique within the same scope.  

## Chapter two  
...

## Chapter three

### 1.1 parsing principle

Three things that program source code will happend before execute:
1. Tokenizing/Lexing  
将字符串分解为有意义代码块 每一块为一个单元token. ie: var a = 2 => var， a，=， 2， ；。
2. Parsing  
将词法单元流（数组）转换为AST（语法树， 由元素逐级嵌套所组成的代表语法结构的树）
3. Generate code  
AST => executable code for system
  
### 1.2 Scope  
