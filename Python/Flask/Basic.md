## Mini server:
```
from flask import Flask
app = Flask(__name__) 

# 第一个参数是应用模块或者包的名称。 如果你使用单一的模块（如本例），你应该使用 __name__ ，因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同

@app.route('/')
def h_w():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__'确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。

# 如果你禁用了 debug 或信任你所在网络的用户，你可以简单修改调用 run() 的方法使你的服务器公开可用，如下:
app.run(host='0.0.0.0')
这会让操作系统监听所有公网 IP。

# app.run(debug=True) 调试模式类似HRM
```

## Router
route() 装饰器把一个**函数**绑定到对应的 URL 上。

### Variable Rules
```
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath
```

## URL Building
```
>>> with app.test_request_context():
...  print url_for('index')
...  print url_for('login')
...  print url_for('login', next='/')
...  print url_for('profile', username='John Doe')
...
/
/login
/login?next=/
/user/John%20Doe
```

### HTTP methods
```
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```

### Static Files
```
url_for('static', filename='style.css')
```
The file has to be stored on the filesystem as static/style.css.  

## Rendering Templates
Flask 配备了 Jinja2 模板引擎  
你可以使用 render_template() 方法来渲染模板。
```
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
