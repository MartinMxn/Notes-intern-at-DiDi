## Array-like obj
例如arguments 的元素，有 length 属性，但不能用一些数组的方法，如 push，pop。

### Array-like obj in underscore.js
```
var MAX_ARRAY_INDEX = Math.pow(2, 53) - 1;
var getLength = property('length');
var isArrayLike = function(collection) {
  var length = getLength(collection);
  return typeof length == 'number' && length >= 0 && length <= MAX_ARRAY_INDEX;
  // as long as has length property and is a non-negative number
};
```
### Array-Like to Array
```
function fake() {
  let arr = []
  for (let i = 0; i < arguments.length; i++) {
    arr[i] = arguments[i];
  }
  arr.push(4);
  console.log(arr);
}

fake(1, 2, 3)
```
或者
```
function fake() {
  var arr = Array.prototype.slice.call(arguments);
  // or [] to replace Array.prototype
  var arr = [].slice.call(arguments);
  arr.push(4); // arr -> [1, 2, 3, 4]
}

fake(1, 2, 3);
```
ES6
```
```
