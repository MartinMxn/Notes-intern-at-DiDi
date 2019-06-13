## Functional preparation:
underscore最外层是一个立即执行函数
(function () {...}) (); // 立即执行函数
利用了JavaScript的函数作用域的概念。这样可以防止其他代码对该函数内部造成影响，而且不会创造全局变量防止污染全局空间。
```
var root = this;

// 保存原有全局变量“_”
var previousUnderscore = root._;

// 使用noConflict方法返回自身
_.noConflict = function() {
  root._ = previousUnderscore;
  return this;
};

// Symbol是ecma262第6版才正式发布的，所以要先判断是否存在。
var SymbolProto = ((typeof(Symbol)) !== ("undefined")) ? (Symbol.prototype) : (null);

var ArrayProto = Array.prototype, ObjProto = Object.prototype, FuncProto = Function.prototype;
var
    push             = ArrayProto.push,
    slice            = ArrayProto.slice,
    concat           = ArrayProto.concat,
    toString         = ObjProto.toString,
    hasOwnProperty   = ObjProto.hasOwnProperty;
All ECMAScript 5 native function implementations that we hope to use are declared here.
  var
    nativeIsArray      = Array.isArray,
    nativeKeys         = Object.keys,
    nativeBind         = FuncProto.bind;
```

检测集合迭代器
```
var builtinIteratee;  // 设置变量保存内置迭代

var cb = function(value, context, argCount) {
  if (_.iteratee !== builtinIteratee) return _.iteratee(value, context);  // 如果用户修改了迭代器，则使用新的迭代器
  if (value == null) return _.identity;  // 如果不传value，表示返回等价的自身
  if (_.isFunction(value)) return optimizeCb(value, context, argCount);  // 如果传入函数，返回该函数的回调
  if (_.isObject(value)) return _.matcher(value);  // 如果传入对象，寻找匹配的属性值
  return _.property(value);  // 如果都不是，返回相应的属性访问器
};
  
// 默认的迭代器，是以无穷argCount为参数调用cb函数。用户可以自行修改。
_.iteratee = builtinIteratee = function(value, context) {
  return cb(value, context, Infinity);
};
```

检测是否是node.js环境，是则作为一个模块输出
```
if (typeof exports != 'undefined' && !exports.nodeType) {
  if (typeof module != 'undefined' && !module.nodeType && module.exports) {
  exports = module.exports = _;
  }
  exports._ = _;
} else {
  root._ = _;
}
```

## _.each、_.forEach
```

```
