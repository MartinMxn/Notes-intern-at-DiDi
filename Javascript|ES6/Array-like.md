## Array-like obj in underscore.js

```
var MAX_ARRAY_INDEX = Math.pow(2, 53) - 1;
var getLength = property('length');
var isArrayLike = function(collection) {
  var length = getLength(collection);
  return typeof length == 'number' && length >= 0 && length <= MAX_ARRAY_INDEX;
};
```
有length属性的obj，且属性值为非负 Number 类型即可

## Array-Like to Array
```
function fn() {
  var arr = [];
  for (var i = 0, len = arguments.length; i < len; i++)
    arr[i] = arguments[i];

  arr.push(4); 
  // [1, 2, 3, 4]
}

fn(1, 2, 3);
```

or more elegant
```
function fn() {
  var arr = Array.prototype.slice.call(arguments);
  // or 
  var arr = [].slice.call(arguments);
  arr.push(4); // arr -> [1, 2, 3, 4]
}

fn(1, 2, 3);
```

// And in ES6
```
var str = "helloworld";
var arr = Array.from(str); 
// ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
```
