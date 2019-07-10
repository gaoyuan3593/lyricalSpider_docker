__author__ = 'gaoy'


class DottableDict(dict):
    def __getattr__(self, key):
        if key in self.keys():
            v = self.get(key, None)
            if v and isinstance(v, dict):
                return DottableDict(v)
        return self.get(key, None)


def enum(**named_values):
    return type('Enum', (), named_values)


class Switch(object):
    def __init__(self, v):
        self.v = v
        self.fail = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fail or not args:
            return True
        elif self.v in args:
            self.fail = True
            return True
        else:
            return False
