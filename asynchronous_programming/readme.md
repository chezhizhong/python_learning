# **asynchronous programming**
异步编程的好处非常明显，就是可以提高运行效率。归根结底，异步都是基于协程进行的。

## **协程**

协程也被称为微线程，是一种用户态内的上下文切换技术，简而言之就是通过一个线程实现代码块的相互切换执行。协程不是计算机提供的，是程序员人为创造的。

> 注意： 上下文切换的方式见context_switch.py文件

## **事件循环**

事件循环可以理解为一个死循环，去检测并执行某些代码

如果某个任务处于IO操作，事件循环认定该任务为不可执行任务

## **协程函数和协程对象**

```python
async def func():  # 协程函数
    pass
result = func()  # 协程对象，这个时候程序是不会执行的
```
> 如果想要运行协程函数内部的代码，必须要将协程对象交给事件循环来处理

```python
import asyncio
async def func():
    print('let us go')
result = func()
loop = asyncio.get_event_loop()
loop.run_until_complete(result)
```
> 放入事件循环的方式有两种：
```
# 第一种：
loop = asyncio.get_event_loop()
loop.run_until_complete(result)
# 第二种：
asyncio.run(result)  # python3.7后才有的用法
```

## **await关键字**

await声明程序挂起，等待协程对象的值得到之后再继续向下执行

await + 可等待对象
> 可等待对象包含：协程对象、Future、Task对象

## **task对象**

简单点就是在事件循环中添加多个任务，用于并发调度协程

```python
import asyncio
# 第一种方式  python3.7以后才引入该用法
asyncio.create_task(coroutine_obj)
# 第二种方式
loop = asyncio.get_event_loop()
loop.create_task(coroutine_obj)
# 第三种方式
loop.ensure_future(coroutine_obj)
```
使用案例见coroutine_example.py

## **future对象**

task继承future，task对象内部await结果的处理基于future对象来的

使用案例见coroutine_example.py