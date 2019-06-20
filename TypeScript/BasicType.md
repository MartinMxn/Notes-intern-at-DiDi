boolean
```
let isDone: boolean = false;
```
number
和JavaScript一样，TypeScript里的所有数字都是浮点数。  
除了支持十进制和十六进制字面量，TypeScript还支持ECMAScript 2015中引入的二进制和八进制字面量。
```
let decLiteral: number = 6;
let hexLiteral: number = 0xf00d;
let binaryLiteral: number = 0b1010;
let octalLiteral: number = 0o744;
```
string
模版字符串同js
#### 
array
```
let list: number[] = [1, 2, 3];
第二种方式是使用数组泛型，Array<元素类型>：
let list: Array<number> = [1, 2, 3];
```
tuple
表示一个已知元素数量和类型的数组
```
let x: [string, number];
x = ['hello', 10]; // OK
x = [10, 'hello']; // Error

访问一个已知索引的元素，会得到正确的类型
console.log(x[0].substr(1)); // OK
console.log(x[1].substr(1)); // Error, 'number' does not have 'substr'

当访问一个越界的元素，会使用联合类型替代
x[3] = 'world'; // OK, 字符串可以赋值给(string | number)类型
console.log(x[5].toString()); // OK, 'string' 和 'number' 都有 toString
x[6] = true; // Error, 布尔不是(string | number)类型
```
