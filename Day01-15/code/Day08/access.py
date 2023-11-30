class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()

'''
Github Copilot
`access.py`中的代码是Python中私有属性和私有方法的使用示例。

在这个例子中，定义了一个名为`Test`的类，它有一个私有属性`__foo`和一个私有方法`__bar`。在Python中，以双下划线`__`开头的属性和方法被视为私有的，它们不能被直接访问。

`__init__`方法是类的构造方法，当创建`Test`类的实例时，会自动调用这个方法。在这个方法中，将传入的参数`foo`赋值给私有属性`__foo`。

私有方法`__bar`中，打印了私有属性`__foo`的值和字符串'__bar'。

在`main`函数中，创建了一个`Test`类的实例`test`，并尝试访问其私有方法和私有属性。由于私有方法和属性不能直接访问，所以这里使用了一个特殊的语法`_类名__方法名`和`_类名__属性名`来访问它们。这是Python的一个特性，虽然可以这样做，但并不推荐在正常的类外部代码中使用。

最后，调用`main`函数执行上述操作。

'''