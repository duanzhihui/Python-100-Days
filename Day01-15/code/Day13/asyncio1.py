"""
异步I/O操作 - asyncio模块

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

import asyncio
import threading
# import time


@asyncio.coroutine
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有yield from才会等待休眠操作执行完成
    yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()

'''
`asyncio`模块提供了许多方法和类来处理异步I/O操作。以下是一些主要的方法：

1. **`asyncio.run(coro, *, debug=False)`**：这是从Python 3.7开始引入的一个方便的函数，用于执行一个协程并返回结果。它会自动创建一个事件循环，运行传入的协程，然后关闭事件循环。

2. **`asyncio.create_task(coro, *, name=None)`**：这个函数用于创建一个`Task`对象，它包装了一个协程，并将其排入事件循环的执行计划中。返回的`Task`对象可以用于获取协程的结果，或者取消协程的执行。

3. **`asyncio.sleep(delay, result=None, *, loop=None)`**：这是一个协程，它会在指定的延迟时间后返回指定的结果。这个协程不会阻塞事件循环。

4. **`asyncio.wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED)`**：这个函数返回一个协程，它会等待一个由`Future`或协程构成的可迭代对象。`return_when`参数指定了何时返回。

5. **`asyncio.gather(*aws, loop=None, return_exceptions=False)`**：这个函数返回一个协程，它会并行运行传入的所有`aws`（`Future`对象或协程），并在所有`aws`都完成时返回一个结果列表。

6. **`asyncio.get_event_loop()`**：这个函数返回当前线程的事件循环。如果当前线程还没有事件循环，它会引发一个`RuntimeError`。

7. **`asyncio.new_event_loop()`**：这个函数创建一个新的事件循环并设置为当前线程的事件循环。

8. **`asyncio.set_event_loop(loop)`**：这个函数设置当前线程的事件循环为`loop`。

9. **`asyncio.open_connection(host=None, port=None, *, loop=None, limit=None, **kwds)`**：这个函数返回一个协程，它会打开一个到指定`host`和`port`的连接。

10. **`asyncio.start_server(client_connected_cb, host=None, port=None, *, loop=None, **kwds)`**：这个函数返回一个协程，它会创建一个服务器，当有新的连接时，会调用`client_connected_cb`回调函数。

以上是`asyncio`模块的一些主要方法，但还有许多其他的类和函数，如`Protocol`、`Transport`、`StreamReader`、`StreamWriter`等，可以用于更复杂的异步I/O操作。
'''