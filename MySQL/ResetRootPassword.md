# Reset Root Password

## 1. 关闭正在运行的MySQL(如果开启状态)
在终端输入下面命令关闭正在运行的mysql，如果msyql没有运行可以跳过，需要输入mysql的密码。  
```
/usr/local/mysql/bin/mysqladmin -u root -p shutdown  
```
如果mysql密码忘记了，可以直接通过系统偏好设置里面关闭！  

## 2. 进入mysql的bin目录执行如下命令
```
$ cd /usr/local/mysql/bin 
$ sudo su  
```
之后输入管理员密码会看到
```
sh-3.2# 
```
之后我们输入下面命令以安全模式运行mysql
```
sh-3.2#./mysqld_safe --skip-grant-tables &
```

运行结束我们打开mac的系统偏好设置，选择msyql，我们会发现Mysql重新运行  
回到终端点击Command ＋ N 重新打开一个终端   
输入
```
mysql -u -root
```
这时候我们不需要密码就能进入mysql

## 3. 修改root密码
先执行下面命令为了能够修改任意的密码
```
mysql> FLUSH PRIVILEGES;
 ```
之后执行修改密码的SQL语句, 123456可以替换你自己想要修改的密码
```
mysql> SET PASSWORD FOR root@'localhost' = PASSWORD('123456');
```
最后刷新
```
mysql> FLUSH PRIVILEGES;
```
Control＋D推出mysql，然后关闭安全模式数据库，这里要输入你刚才设置数据密码  
```
/usr/local/mysql/bin/mysqladmin -u root -p shutdown
```
在偏好设置重启MySQL服务器
```
mysql -u root -p
```
使用新密码登录
