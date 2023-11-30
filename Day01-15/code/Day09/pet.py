from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()


'''
`ABCMeta` 和 `abstractmethod` 都是 Python 的 `abc` 模块中的一部分，用于实现抽象基类。

`ABCMeta` 是一个元类，用于定义抽象基类。在 Python 中，元类是创建类的“东西”。你可以通过将 `ABCMeta` 作为元类来创建一个抽象基类。这样，这个类就不能被实例化，只能被其他类继承。

`abstractmethod` 是一个装饰器，用于声明一个方法是抽象的。抽象方法是在抽象类中声明但不实现的方法。子类必须提供这个方法的实现，否则子类也将成为抽象类，不能被实例化。

例如，以下代码定义了一个抽象基类 `Shape`，它有一个抽象方法 `area`：

```python
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        pass
```

任何试图实例化 `Shape` 的尝试都会失败，除非定义一个继承 `Shape` 的子类并实现 `area` 方法。
'''