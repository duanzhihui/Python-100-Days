"""
异步I/O操作 - asyncio模块

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 异步方式等待连接结果
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # 异步I/O方式执行写操作
    await writer.drain()
    while True:
        # 异步I/O方式执行读操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
# 通过生成式语法创建一个装了三个协程的列表
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
# 下面的方法将异步I/O操作放入EventLoop直到执行完毕
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
这些代码片段主要展示了Python的异步I/O操作，特别是`asyncio`模块的使用。

在`asyncio1.py`中，定义了一个名为`hello`的协程，它首先打印当前线程的信息，然后异步地等待2秒，再打印当前线程的信息。这个协程被调用两次并放入一个任务列表中，然后使用`asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))`来运行这些任务，直到所有任务完成。

`asyncio2.py`中的代码与`asyncio1.py`非常相似，但是使用了`async`和`await`关键字，这是Python 3.5引入的新语法，用于定义协程和等待协程完成。

`asyncio3.py`中的代码展示了如何使用`asyncio`模块进行网络I/O操作。定义了一个名为`wget`的协程，它首先打开一个到指定主机的连接，然后发送一个HTTP GET请求，读取响应头部，并打印出来。这个协程对每个在`hosts_list`中的主机进行操作，所有的协程都被放入一个任务列表中，然后使用`asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))`来运行这些任务，直到所有任务完成。

总的来说，这些代码展示了Python的异步编程能力，特别是如何使用`asyncio`模块进行异步I/O操作。
'''
# centos 统计文件夹大小
du -sh *