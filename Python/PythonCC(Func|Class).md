## Function
```
def greet_user(username):  # 形参
  print(username)
  
greet_user('jesse') # 实参
```

**位置实参** ，这要求实参的顺序与形参的**顺序**相同；
也可使用**关键字实参** ，其中每个实参都由变量名和值组成；
```
describe_pet(animal_type='hamster', pet_name='harry')
```

**默认值**
```
def describe_pet(pet_name, animal_type='dog'):
"""显示宠物的信息"""
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
```

```
def get_formatted_name(first_name, last_name, middle_name=''):
"""返回整洁的姓名"""
  if middle_name:
    full_name = first_name + ' ' + middle_name + ' ' + last_name
  else:
    full_name = first_name + ' ' + last_name
  return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

### 传递任意数量的实参
```
def make_pizza(*toppings):
"""打印顾客点的所有配料"""
  print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
形参名*toppings 中的星号让Python创建一个名为toppings 的***空元组**，并将收到的所有值都封装到这个**元组**中

#### 结合使用位置实参和任意数量实参
```
def make_pizza(size, *toppings):
"""概述要制作的比萨"""
  print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
  for topping in toppings:
    print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中

#### 使用任意数量的关键字实参
```
def build_profile(first, last, **user_info):
  """创建一个字典，其中包含我们知道的有关用户的一切"""
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  for key, value in user_info.items():
    profile[key] = value
  return profile
  
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
```
形参**user_info 中的两个星号让Python创建一个名为user_info 的**空字典**，并将收到的所有名称—值对都封装到这个字典中。

### 将函数存储在模块中
```
导入
pizza.py ⬇️
---------------------
def make_pizza(size, *toppings):
  """概述要制作的比萨"""
  print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
for topping in toppings:
  print("- " + topping)
---------------------
```
```
making_pizzas.py ⬇️
---------------------
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
----------------------
```
#### 导入特定的函数
```
from module_name import function_name
from module_name import function_0, function_1, function_2
```
#### 用as 给函数指定别名
```
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```
#### 使用as 给模块指定别名
```
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
#### 导入模块中的所有函数
```
from pizza import *
```
