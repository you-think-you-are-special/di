from inspect import signature


def names(method):
    args = signature(method).parameters.items()
    return list(map(lambda s: s[0], list(args)))
