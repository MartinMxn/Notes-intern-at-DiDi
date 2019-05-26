## Chapter One
### Prefix for CSS
-moz= => Firefox  
-ms- => IE  
-o- => Opera  
-webkit- => Chrome, Safari  

### Code Skill for CSS
**Try to minimize duplicates**  
```    
  padding: 6px 16px;
  border: 1px solid #446d88;
  background: #58a;
  border-radius: 4px;
  box-shadow: 0 1px 5px gray;
  color: white;
  text-shadow: 0 -1px 1px #335166;
  font-size: 20px;
  line-height: 30px;
  outline: none;
```
Sth need to fix:  
1. If there are some relationship between some values, it should be showed as relationship
```
  font-size: 20px;
  line-height: 1.5;
```
2. Abs font size is ez to manipulate but not good for later modification
```
  font-size: 125%; // If we change size of parents size, this will also changed
  line-height: 1.5;
```
3. All related unit from px to em(or rem depends on situation)
```
  padding: .3em .8em;
  border: 1px solid #446d88;  /* we dont want border width changed by size */
  background: #58a;
  border-radius: .2e,;
  box-shadow: 0 .05em .25em gray;
  color: white;
  text-shadow: 0 -05em 0.5em #335166;
  font-size: 20px;
  line-height: 30px;
  outline: none;
```
