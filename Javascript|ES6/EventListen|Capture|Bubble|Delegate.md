## 事件监听 
### element.addEventListener(< event-name >, < callback >, < use-capture >);
当监听到有 < event-name > 事件发生的时候，调用 < callback > 这个回调函数。< use-capture > 表示该事件监听是在**捕获**阶段中监听（true 捕获阶段）还是在**冒泡**阶段中监听（false 冒泡阶段）。  
## 移除事件监听 
### element.removeEventListener(< event-name >, < callback >, < use-capture >);
移除事件监听时的回调函数**不能是匿名函数**

Event dispatch and DOM event flow (From W3C):  
<img src="https://www.w3.org/TR/DOM-Level-3-Events/images/eventflow.svg" width="400">

## 捕获阶段（Capture Phase）
当有事件被触发时，发生的顺序为从window发出到目标节点，在此之前的过程就是事件捕获阶段，**所有经过的节点都会触发这个事件。**

## 目标阶段（Target Phase）
当事件到达目标节点，最终在目标节点触发时为目标阶段，需注意这个事件触发**总在最底层节点。**  
eg:  
```
<div onclick="function a(){...}">
  <p><p>
  <div><span></span></div>
</div>
```
div的点击事件实际触发在p和span上  ***need example here:***

## 冒泡阶段（Bubbling Phase)  
事件达到目标节点之后，沿着原路返回的阶段

A excellent expamle click <a href="http://jsbin.com/exezex/4/embed?css,js,output">here</a>

## 第三个参数 
默认为false 在冒泡阶段监听，不常用是因为IE浏览器不支持在捕获阶段监听，

## 使用事件代理（委托）（Event Delegate）提升性能 
因为事件冒泡机制，所有子节点的事件都会顺着父级节点跑回去，所以可以通过监听父级节点来实现监听子节点的功能，这就是事件代理。
使用事件代理主要有两个优势： 
1. 减少事件绑定，提升性能。之前你需要绑定一堆子节点，而现在你只需要绑定一个父节点即可。减少了绑定事件监听函数的数量。 
2. 动态变化的 DOM 结构，仍然可以监听。当一个 DOM 动态创建之后，不会带有任何事件监听，除非你重新执行事件监听函数，而使用事件监听无须担忧这个问题。
