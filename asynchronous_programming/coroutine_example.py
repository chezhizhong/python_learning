import requests
import aiohttp
import asyncio


class NormalDownload:
    def __init__(self):
        pass

    @staticmethod
    def download_image(url):
        print('开始下载：', url)
        response = requests.get(url)
        print('下载完成.')
        file_name = url.split('/')[-1]
        file_name = file_name if len(file_name.split('.')) == 2 else file_name.split('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(response.content)

    def __call__(self, *args, **kwargs):
        url_list = [
            'https://img95.699pic.com/photo/50136/1351.jpg_wh300.jpg',
            'https://img.yalayi.net/d/file/2021/48679tuku05/z1.jpg'
        ]
        for item in url_list:
            self.download_image(item)


class AsyncDownload:
    def __init__(self):
        pass

    @staticmethod
    async def fetch(session, url):
        print('发送请求： ', url)
        async with session.get(url, verify_ssl=False) as response:
            content = await response.content.read()
            file_name = url.split('/')[-1]
            file_name = file_name if len(file_name.split('.')) == 2 else file_name.split('_')[-1]
            with open(file_name, mode='wb') as file_object:
                file_object.write(content)

    async def main(self):
        async with aiohttp.ClientSession() as session:
            url_list = [
                'https://img95.699pic.com/photo/50136/1351.jpg_wh300.jpg',
                'https://tu.sioe.cn/gj/qiege/image.jpg'
            ]
            tasks = [asyncio.create_task(self.fetch(session, url)) for url in url_list]
            await asyncio.wait(tasks)

    def __call__(self, *args, **kwargs):
        asyncio.run(self.main())


class AwaitKey:
    def __init__(self):
        pass

    async def func1(self):
        print('func1')
        response = await asyncio.sleep(2)
        print('end: ', response)

    async def others(self):
        print('start')
        await asyncio.sleep(2)
        print('end')
        return 'return'

    async def func2(self):
        print('执行协程函数内部代码')
        response = await self.others()
        print('IO等待结束，结果为： ', response)

    async def func3(self):
        print('执行协程函数内部代码')
        response = await self.others()
        print('IO等待结束，结果为： ', response)
        response1 = await self.others()
        print('IO等待结束，结果为： ', response1)

    def __call__(self, *args, **kwargs):
        # asyncio.run(self.func1())
        # asyncio.run(self.func2())
        asyncio.run(self.func3())


class TaskObj:
    def __init__(self):
        pass

    async def func1(self):
        print('start')
        await asyncio.sleep(2)
        print('end')
        return 'return'

    async def main1(self):
        print('main1 start')
        task1 = asyncio.create_task(self.func1())
        task2 = asyncio.create_task(self.func1())
        print('main1 end')
        ret1 = await task1
        ret2 = await task2
        print(ret1, ret2)

    async def main2(self):
        print('main2 start')
        task_list = [
            asyncio.create_task(self.func1()),
            asyncio.create_task(self.func1())
        ]
        print('main2 end')
        done, pending = await asyncio.wait(task_list, timeout=None)
        print(done)

    def main3(self):
        print('main3 start')
        task_list = [
            self.func1(),
            self.func1()
        ]
        print('main3 end')
        done, pending = asyncio.run(asyncio.wait(task_list, timeout=None))
        print(done)

    def __call__(self, *args, **kwargs):
        # asyncio.run(self.main1())
        # asyncio.run(self.main2())
        self.main3()


class FutureObj:
    def __init__(self):
        pass

    async def main1(self):
        loop = asyncio.get_event_loop()
        fut = loop.create_future()
        await fut

    async def set_after(self, fut):
        await asyncio.sleep(2)
        fut.set_result('666')

    async def main2(self):
        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        await loop.create_task(self.set_after(fut))
        data = await fut
        print(data)

    def __call__(self, *args, **kwargs):
        asyncio.run(self.main1())
        asyncio.run(self.main2())


if __name__ == '__main__':
    # normal_obj = NormalDownload()
    # normal_obj()
    # async_obj = AsyncDownload()
    # async_obj()
    # await_obj = AwaitKey()
    # await_obj()
    task_obj = TaskObj()
    task_obj()
