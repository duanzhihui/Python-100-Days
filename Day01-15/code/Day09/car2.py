"""
属性的使用
- 使用已有方法定义访问器/修改器/删除器

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self.set_brand(brand)
        self.set_max_speed(max_speed)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)

    # 用已有的修改器和访问器定义属性
    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)


car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
print(car)
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)

"""
在Python中，`property()`是一个内置函数，用于获取、设置或删除对象的属性。它返回一个属性值，这个属性值有三个方法，分别是getter方法、setter方法和deleter方法。

`property()`函数的基本语法如下：

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

- `fget`：用来获取属性值的函数。
- `fset`：用来设置属性值的函数。
- `fdel`：用来删除属性值的函数。
- `doc`：一个可选参数，用于设置属性的文档字符串。

在你的代码中：

```python
brand = property(get_brand, set_brand)
max_speed = property(get_max_speed, set_max_speed)
```

`brand`和`max_speed`都是使用`property()`函数定义的属性。`get_brand`和`set_brand`是`brand`属性的getter和setter方法，`get_max_speed`和`set_max_speed`是`max_speed`属性的getter和setter方法。

当你尝试获取`brand`或`max_speed`属性的值时，会自动调用对应的getter方法；当你尝试设置`brand`或`max_speed`属性的值时，会自动调用对应的setter方法。这样，你就可以在getter和setter方法中添加任何你需要的代码，例如数据验证或错误处理。

"""

