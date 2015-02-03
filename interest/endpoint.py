import asyncio


class Endpoint:

    # Public

    def __init__(self, coro, *, path, methods):
        self.__coro = coro
        self.__path = path
        self.__methods = methods

    @asyncio.coroutine
    def __call__(self, request, **kwargs):
        return (yield from self.__coro(request, **kwargs))

    def __repr__(self):
        template = (
            '<Endpoint path="{self.path}" methods="{self.methods}">')
        compiled = template.format(self=self)
        return compiled

    @property
    def path(self):
        return self.__path

    @property
    def methods(self):
        return self.__methods