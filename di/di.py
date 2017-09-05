import di.args as args


class DI(object):
    def __init__(self):
        self._dependencies = {}
        self._factories = {}

    def register(self, name: str, instance):
        self._dependencies[name] = instance

    def factory(self, name: str, factory):
        self._factories[name] = factory

    def get(self, name: str):
        in_facs = name in self._factories

        if in_facs:
            self._dependencies[name] = self._inject(self._factories[name])

        in_deps = name in self._dependencies

        if not in_deps:
            raise ModuleNotFoundError('Cannot find module: %s' % name)

        return self._dependencies[name]

    def _inject(self, factory):
        arg_names = args.names(factory)
        deps = list(map(lambda arg: self.get(arg), arg_names))
        return factory(*deps)

    def contains(self, name):
        return name in self._dependencies

    def __getitem__(self, item):
        return self.get(item)

    def __getattr__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return self.contains(item)
