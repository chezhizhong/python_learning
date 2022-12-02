import asyncio
from greenlet import greenlet


"""
greenlet（早期模块）
"""


class GreenletSwitch:
    def __init__(self):
        self.gr1 = greenlet(self.func1)
        self.gr2 = greenlet(self.func2)

    def func1(self):
        print(1, end=' ')
        self.gr2.switch()
        print(2, end=' ')
        self.gr2.switch()

    def func2(self):
        print(3, end=' ')
        self.gr1.switch()
        print(4)

    def __call__(self, *args, **kwargs):
        self.gr1.switch()


"""
使用关键字yield
"""


class YieldSwitch:
    def __init__(self):
        pass

    def func1(self):
        yield 1
        yield from self.func2()
        yield 2

    def func2(self):
        yield 3
        yield 4

    def __call__(self, *args, **kwargs):
        f1 = self.func1()
        for item in f1:
            print(item, end=' ')
        print()


"""
asyncio装饰器（python3.4）
"""


class AsyncioSwitch:
    """
    @asyncio.coroutine装饰过的函数变成了协程函数，func()的方式无法执行函数
    必须要将函数放在loop.run_until_complete()里面才能正确执行
    该方法的优点是遇到IO就自动切换
    """
    def __init__(self):
        pass

    @asyncio.coroutine
    def func1(self):
        print(1, end=' ')
        yield from asyncio.sleep(2)
        print(2, end=' ')

    @asyncio.coroutine
    def func2(self):
        print(3, end=' ')
        yield from asyncio.sleep(2)
        print(4)

    def __call__(self, *args, **kwargs):
        tasks = [
            asyncio.ensure_future(self.func1()),
            asyncio.ensure_future(self.func2())
        ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))


"""
async、await关键字（python3.5）
"""


class AsyncSwitch:
    def __init__(self):
        pass

    async def func1(self):
        print(1, end=' ')
        await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务
        print(2, end=' ')

    async def func2(self):
        print(3, end=' ')
        await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务
        print(4)

    def __call__(self, *args, **kwargs):
        tasks = [
            asyncio.ensure_future(self.func1()),
            asyncio.ensure_future(self.func2())
        ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    greenlet_obj = GreenletSwitch()
    greenlet_obj()
    yield_obj = YieldSwitch()
    yield_obj()
    asyncio_obj = AsyncioSwitch()
    asyncio_obj()
    async_obj = AsyncSwitch()
    async_obj()
