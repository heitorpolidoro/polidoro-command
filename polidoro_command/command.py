import inspect


# noinspection PyPep8Naming
class Command:
    def __init__(self, method, args, kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs
        self.kwargs.setdefault("help", "")

    @property
    def method_name(self):
        return self.method.__name__

    def __getattr__(self, item):
        return self.kwargs.get(item)

    @property
    def clazz(self):
        method = self.method
        if inspect.ismethod(method):
            for cls in inspect.getmro(method.__self__.__class__):
                if cls.__dict__.get(method.__name__) is method:
                    return cls
            method = method.__func__  # fallback to __qualname__ parsing
        if inspect.isfunction(method):
            try:
                cls = getattr(inspect.getmodule(method),
                              method.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
                if isinstance(cls, type):
                    return cls
            except AttributeError:
                pass
        return getattr(method, '__objclass__', None)


def command(*args, **kwargs):
    from polidoro_command import PolidoroArgumentParser
    if len(args) == 1 and callable(args[0]):
        method = args[0]
        PolidoroArgumentParser.add_command(Command(method, args[1:], kwargs))
        return method
    else:
        def command_wrapper(method_):
            return command(method_, *args, **kwargs)
        return command_wrapper
