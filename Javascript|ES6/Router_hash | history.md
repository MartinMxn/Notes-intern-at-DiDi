# 单页应用的两种路由 hash和history  

## Hash
hash 就是指 url 尾巴后的 # 号以及后面的字符,  hash 值变化不会导致浏览器向服务器发出请求  
而且 hash 改变会触发 hashchange 事件，浏览器的进后退也能对其进行控制  
相当于添加了一项访问历史记录  
```
window.addEventListener('hashchange', function(){ 
    // 监听hash变化，点击浏览器的前进后退会触发
})

or

window.onhashchange = function(event){
     console.log(event.oldURL, event.newURL);
     // oldURL and newURL are two read-only properities of event in hashchange fucntion
     let hash = location.hash.slice(1);  // after #, so 1
     document.body.style.color = hash;
}
```
### 浏览器发送请求不会携带#后面内容，所以刷新或者其他操作不会影响请求地址

#### 拓展：SEO优化与爬虫获取url地址问题

hash 能兼容到IE8， history 只能兼容到 IE10

## History 
Why History？  
1. 如果拿来做路由的话，原来的锚点功能就不能用了
2. 其次，hash 的传参是基于 url 的，如果要传递复杂的数据，会有体积的限制(chrome 8182bytes)
而 history 模式不仅可以在url里放参数，还可以将数据存放在一个特定的对象中。

#### history 接口是 HTML5 新增的，它有五个方法可以改变 url 而不刷新页面  
#### window.location.search 返回?后面包括?的字符串  

window.history:
Properities:  
#### History.length 只读
返回一个int，该整数表示会话历史中元素的数目，包括当前加载的页。例如，在一个新的选项卡加载的一个页面中，这个属性返回1。
每加载一个页面+1
#### History.scrollRestoration 
允许Web应用程序在历史导航上显式地设置默认滚动恢复行为。此属性可以是自动的（auto）或者手动的（manual）。
#### History.state 只读
返回一个表示历史堆栈顶部的状态的值。这是一种可以不必等待popstate 事件而查看状态而的方式。  
例子在下面

#### History.back()
前往上一页, 用户可点击浏览器左上角的返回按钮模拟此方法. 等价于 history.go(-1).  
Note: 当浏览器会话历史记录处于第一页时调用此方法没有效果，而且也不会报错。  
#### History.forward()
在浏览器历史记录里前往下一页，用户可点击浏览器左上角的前进按钮模拟此方法. 等价于 history.go(1).  
Note: 当浏览器历史栈处于最顶端时( 当前页面处于最后一页时 )调用此方法没有效果也不报错。  
#### History.go()
通过当前页面的相对位置从浏览器历史记录( 会话记录 )加载页面。比如：参数为-1的时候为上一页，参数为1的时候为下一页.   
当输入为空或超出界限是也不会报错但无效  

#### History.pushState(stateObj, title, url)  
#### History.replaceState(stateObj, title, url)  
url could be absolute, but relative is better  
if not in same origin, would throw an error  
#### 
replaceState()  是修改了当前的历史记录项而不是新建一个。 注意这并不会阻止其在全局浏览器历史记录中创建一个新的历史记录项。
使用场景在于为了响应用户操作，你想要更新状态对象state或者当前历史记录的URL。

These methods work in conjunction with the window.onpopstate event.  
 每当活动的历史记录项发生变化时， popstate 事件都会被传递给window对象。
 如果当前活动的历史记录项是被 pushState 创建的，或者是由 replaceState 改变的，那么 popstate 事件的状态属性 state 会包含一个当前历史记录状态对象的拷贝。
