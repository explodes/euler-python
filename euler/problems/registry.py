REGISTRY = []


def register(klass):
    REGISTRY.append(klass)
    return klass
