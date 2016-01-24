# Submitter: dparajul(Parajuli, Darshan)

from collections import defaultdict


class Bag:
    def __init__(self, contents=None):
        self._contents = defaultdict(int)
        if contents is not None:
            for i in contents:
                self._contents[i] += 1

    def __repr__(self):
        return 'Bag({})'.format(self._as_list())

    def __str__(self):
        return 'Bag({})'.format(','.join(['{}[{}]'.format(k, v) for k, v in self._contents.items()]))

    def __len__(self):
        return sum(v for v in self._contents.values())

    def unique(self):
        return len(self._contents)

    def __contains__(self, item):
        return self._contents.get(item, None) is not None

    def count(self, arg):
        return self._contents.get(arg, 0)

    def add(self, arg):
        self._contents[arg] += 1

    def __add__(self, right):
        if type(right) is not Bag:
            raise TypeError('Type mismatch: {}'.format(right))
        return Bag(self._as_list() + right._as_list())

    def remove(self, key):
        if key not in self._contents:
            raise ValueError('Key: {} not found'.format(key))
        self._contents[key] -= 1
        if self._contents[key] == 0:
            del self._contents[key]

    def __eq__(self, other):
        if type(other) is not Bag:
            return False
        for k, v in self._contents.items():
            if other._contents.get(k) != v:
                return False
        return True

    def __nq__(self, other):
        return type(other) is not Bag or not self.__eq__(other)

    def __iter__(self):
        return self._as_list().__iter__()

    def _as_list(self):
        return [k for k, v in self._contents.items() for _ in range(v)]


if __name__ == '__main__':
    # You can put your own code to test Bags here

    print()
    import driver

    driver.default_file_name = 'bsc1.txt'
    # driver.default_show_exception = True
    # driver.default_show_exception_message = True
    # driver.default_show_traceback = True
    driver.driver()
