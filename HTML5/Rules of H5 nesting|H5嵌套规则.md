# HTML5标签嵌套规则

## Latest version of nesting rules for HTML5 is
```https://www.w3.org/TR/html/dom.html#content-models... ```
```But it's toooooooo complex.```

## Olddddder version (for HTML4/xHTML1)
```Might be useful enough now.```

Categorize tags as ***block*** and ***inline*** tags, commonly see like:    

**block:**
div, p, form, h1~h6, noscript, ol, ul, hr,table
address, blockquote, center, dir, dl, dt, dd, fieldse, isindex, menu, noframes, noscrip, pre ...

**inline:**
a, span, i, img, input, textarea, br, label, select, strong
abbr, acronym, b, bdo, big, br, cite, code, dfn, em, font, kbd, q, s, samp, small, strike, sub, sup, tt, u, var...

inline-block: img, input
display as inline tag but could change width and hight


Details for tags:  
<img src="https://github.com/MartinMxn/Notes-intern-at-DiDi/blob/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-05-25%20%E4%B8%8A%E5%8D%8811.18.01.png" width="400">  
<img src="https://github.com/MartinMxn/Notes-intern-at-DiDi/blob/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-05-25%20%E4%B8%8A%E5%8D%8811.18.19.png" width="400">  
<img src="https://github.com/MartinMxn/Notes-intern-at-DiDi/blob/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-05-25%20%E4%B8%8A%E5%8D%8811.18.32.png" width="400">  
<img src="https://github.com/MartinMxn/Notes-intern-at-DiDi/blob/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-05-25%20%E4%B8%8A%E5%8D%8811.18.42.png" width="400">  
<img src="https://github.com/MartinMxn/Notes-intern-at-DiDi/blob/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-05-25%20%E4%B8%8A%E5%8D%8811.18.54.png" width="400">  

## Rules:  
1. 块级元素与块级元素平级、内嵌元素与内嵌元素平级  
<div><span></span><a></a></div>  // ✅  
<div><span></span><p></p></div>  // ❌ span是行内元素，p是块级元素，所以这个是错误的嵌套  
应改为 <div><div><span></span></div><p></p></div>  
#### 
2. 块元素可以包含内联元素或某些块元素，但内联元素不能包含块元素，它只能包含其它的内联元素  
<div><span></span></div> // ✅  
<span><span></span></span> // ✅  
<span><div></div></span> // ❌ 
<span><p></p></span> // ❌ 
#### 
3. 有几个特殊的块级元素只能包含内嵌元素，不能再包含块级元素  
**h1-h6、p、dt**  
<p><div></div></p> // ❌
