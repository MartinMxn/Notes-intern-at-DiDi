## HTML5 提供了 Canvas 和 SVG 两种绘图技术，也是多数 Web 图表库使用的渲染技术。Canvas 是基于脚本的，通过 JavaScript 指令来动态绘图。而 SVG 则是使用 XML 文档来描述矢量图。

## Canvas
Canvas 提供的绘图能力更底层，适合做到像素级的图形处理，能动态渲染和绘制大数据量的图形。

## Svg
SVG 抽象层次更高，声明描述式的接口功能更丰富，内置了大量的图形、滤镜和动画等，方便进行文档元素的维护，也能导出为文件脱离浏览器环境使用。  
SVG 做定制和交互更有优势

### 性能对比
<a href="https://gw.alipayobjects.com/zos/rmsportal/nNSsPFkNcAoxQTfHfZes.png"></a> 
数据量小 -- SVG 的方案通常内存占用会更小，做缩放、平移等操作的时候往往帧率也更高。  
数据量大 -- Canvas
