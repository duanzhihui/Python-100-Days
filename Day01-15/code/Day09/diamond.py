"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()


if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()

'''
这段代码主要演示了Python中的多重继承和方法解析顺序（MRO）。

在这段代码中，定义了五个类：A、B、C、D和E。其中，A是基类，B和C都继承自A，D继承自B和C，E继承自D。这种继承关系形成了一个菱形（或称为钻石）结构，因此也被称为菱形继承或钻石继承。

在类A和类C中都定义了一个名为`foo`的方法，类B没有定义`foo`方法，所以会继承自A的`foo`方法。类D也没有定义`foo`方法，但由于其继承自B和C，因此在调用`foo`方法时，需要确定到底使用B的`foo`方法还是C的`foo`方法。这就涉及到了Python的方法解析顺序（MRO）问题。

Python解决这个问题的策略是C3线性化，也就是在继承体系中查找方法时，会按照一种特定的顺序，从左到右，一层一层地查找，直到找到为止。

在类E中，通过`super().foo()`调用的是D类的MRO列表中，排在E之后的类的`foo`方法，即C类的`foo`方法。`super(B, self).foo()`调用的是B在E的MRO列表中之后的类的`foo`方法，即A类的`foo`方法。`super(C, self).foo()`调用的是C在E的MRO列表中之后的类的`foo`方法，但是C后面没有定义`foo`方法的类，所以这行代码会抛出`AttributeError`异常。
'''