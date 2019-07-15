## 1. 本地分支修改文件名大小写push后git不删除远程原大小写文件夹
Solution：先删除本地修改的文件夹，push，git会删除大小写文件夹，之后恢复再push一遍即可

## 2. 删除本地分支
```
git branch -d [branchname]
```

## rebase
1. 将多个commit记录合为一个  
2. 将一个branch分支的commit记录添加到另一个branch上，默认在最后
