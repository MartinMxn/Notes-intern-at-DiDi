## boolean
```
let isDone: boolean = false;
```
## number
和JavaScript一样，TypeScript里的所有数字都是浮点数。  
除了支持十进制和十六进制字面量，TypeScript还支持ECMAScript 2015中引入的二进制和八进制字面量。
```
let decLiteral: number = 6;
let hexLiteral: number = 0xf00d;
let binaryLiteral: number = 0b1010;
let octalLiteral: number = 0o744;
```
## string
模版字符串同js
#### 
## array
```
let list: number[] = [1, 2, 3];
第二种方式是使用数组泛型，Array<元素类型>：
let list: Array<number> = [1, 2, 3];
```
## tuple
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
## enum
```
enum Color {Red, Green, Blue}
let c: Color = Color.Green;
默认情况下，从0开始为元素编号。

或者，全部都采用手动赋值：
enum Color {Red = 1, Green = 2, Blue = 4}
let c: Color = Color.Green;
```
## Any
不清楚类型的变量指定一个类型。 可能来自于动态的内容，比如来自用户输入或第三方代码库
```
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // okay, definitely a boolean
```

## Void 
```
与any类型相反
只能为它赋予undefined和null
let unusable: void = undefined;
```

## Null & Undefined
```
let u: undefined = undefined;
let n: null = null;
```

## Never
```
never类型表示的是那些永不存在的值的类型
// 返回never的函数必须存在无法达到的终点
function error(message: string): never {
    throw new Error(message);
}
// 推断的返回值类型为never
function fail() {
    return error("Something failed");
}
```
## Object
除number，string，boolean，symbol，null或undefined之外的类型。
使用object类型，就可以更好的表示像Object.create这样的API。
```
declare function create(o: object | null): void;

create({ prop: 0 }); // OK
create(null); // OK

create(42); // Error
```
## 类型断言/转换
```
let strLength: number = (<string>someValue).length;
let strLength: number = (someValue as string).length;
TypeScript里使用JSX时，只能用as语法。
```
