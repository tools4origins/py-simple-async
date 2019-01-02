import asyncio


class AsyncMetaclass(type):
    def __getattr__(self, name):
        if Async.event_loop is None:
            Async.event_loop = asyncio.new_event_loop()
        return getattr(Async.event_loop, name)


class Async(metaclass=AsyncMetaclass):
    event_loop = None

    def __init__(self):
        raise Exception(
            "This class should not be instantiated, call the class directly, "
            "e.g. Async.run_in_executor(...)"
        )
