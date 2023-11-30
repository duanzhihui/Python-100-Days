"""
另一种创建类的方式

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('骆昊')
    stu1.study('Python程序设计')


if __name__ == '__main__':
    main()  

'''
# Github Copilot
这段代码是使用Python的内建函数`type()`动态创建类的示例。

在这个例子中，`type()`函数用于创建一个新的类型。它需要三个参数：

1. 类名：在这个例子中，类名是'Student'。
2. 父类的元组：在这个例子中，父类是`object`，Python中所有类默认的基类。
3. 类的方法名称与函数绑定的字典：在这个例子中，字典中有两个元素，`__init__`和`study`，它们分别绑定到了函数`bar`和`foo`。

函数`bar`和`foo`分别作为`Student`类的方法，`bar`作为初始化方法，接收一个参数`name`，并将其赋值给`self._name`。`foo`作为`study`方法，接收一个参数`course_name`，并打印一条消息表示学生正在学习的课程。

在`main()`函数中，首先使用`type()`创建了`Student`类，然后创建了一个`Student`类的实例`stu1`，并调用其`study`方法。

最后，调用`main()`函数执行上述操作。
'''