# Object
## 1.Object.keys()  
返回一个数组,包括对象自身的(不含继承的)所有可枚举属性(不含Symbol属性).
#### 在ES5里，如果此方法的参数不是对象（而是一个原始值），那么它会抛出 TypeError。
#### 并且在ES6中，非对象的参数将被强制转换为一个对象。
```
var obj = {'0':'a','1':'b','2':'c'};

Object.keys(obj).forEach(function(key){
   console.log(key,obj[key]);
});
0 a
1 b
2 c
```
## 2.for..in..  
```
var obj = {'0':'a','1':'b','2':'c'};

for(var i in obj) {
   console.log(i,":",obj[i]);
}
```
## 3.Object.getOwnPropertyNames(obj) 同2  
## 4.Reflect.ownKeys(obj)  同1

# Array
## 1. forEach  
## 2. for..in..  
```
var arr=["张三","李四","王五","赵六"];

for (var i in arr){
  console.log(i,":",arr[i]);
}
```
## 3. for-of遍历  
#### 不仅支持数组，还支持大多数类数组对象，例如DOM NodeList对象. 
#### 也支持字符串遍历，它将字符串视为一系列的Unicode字符来进行遍历.
```
var arr=["张三","李四","王五","赵六"];

for (var value of arr){
    console.log(value);
}
```
