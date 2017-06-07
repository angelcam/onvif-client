import asyncio
import time

from onvif.client import ONVIFClient, AsyncONVIFClient


def run_async():
    print("async example")
    print("=============")
    st = time.time()


    loop = asyncio.get_event_loop()

    def handle_future(future):
        print(future.result())

    onvif_client = AsyncONVIFClient(
        host='10.19.57.72',
        port=80,
        username='admin',
        password='Angelcam123',
        loop=loop
    )

    tasks = [onvif_client.device.GetSystemDateAndTime() for i in range(0, 10)]

    future = asyncio.gather(*tasks, return_exceptions=True)

    future.add_done_callback(handle_future)

    loop.run_until_complete(future)
    print("time: %.2f" % (time.time() - st))
    print("=============")


def run_sync():
    print("sync example")
    print("============")
    st = time.time()

    onvif_client = ONVIFClient(
        host='10.19.57.72',
        port=80,
        username='admin',
        password='Angelcam123',
    )

    for i in range(0,10):
        print(onvif_client.device.GetSystemDateAndTime())

    print("Time: %.2f" % (time.time() - st))
    print("=============")


if __name__ == '__main__':
    print("")
    run_async()
    run_sync()

