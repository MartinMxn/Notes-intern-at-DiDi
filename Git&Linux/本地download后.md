1. download后先init git init
修改一定文件或者不修改
2. 切换至不同于master分支 git checkout -b aaa
2. git add/commit 
3. 添加远程 git remote add origin <url>
4. git pull origin master --allow-unrelated-histories
5. git push --set-upstream origin aaa
6. 远程分支merge aaa和master
  本地也可以git merge origin/master --allow-unrelated-histories

远程连接
git remote add github git://github.com/jdoe/coolapp.git
git fetch github

从GitHub的远程分支(PU)创建一个新的本地分支(Test)：
git branch test github/pu
git checkout test

将本地已有的分支 和 远程分支连接
git branch --set-upstream-to=origin/master(远程分支名)  work1(本地分支名)

本地分支存在问题
1. 切换当前分支至另一分支 
checkout -b aa
2. delete 本地master分支
git branch -D master
3. git pull
4. 对修改文件内 command+z撤销 pull的修改并保存
5. push新的到远程master
