# Submitter: dparajul(Parajuli, Darshan)


class Sparse_Matrix:
    def __init__(self, rows, cols, *args):
        assert type(rows) == int and rows > 0 and type(cols) == int and cols > 0, \
            'Illegal values for number of rows and cols: {}, {}'.format(rows, cols)
        self.rows = rows
        self.cols = cols
        self.matrix = dict()
        for r, c, v in args:
            assert type(r) == int and r < rows and type(c) == int and c < cols, \
                'Illegal (row, col) value: ({}, {}).format(r, c)'
            assert type(v) == int or type(v) == float, 'Illegal value type: {}'.format(v)
            if v != 0:
                k = (r, c)
                assert self.matrix.get(k) is None
                self.matrix[k] = v

    def size(self):
        return self.rows, self.cols

    def __len__(self):
        return self.rows * self.cols

    def __bool__(self):
        return any((v != 0) for v in self.matrix.values())

    def __repr__(self):
        return 'Sparse_Matrix({}, {}, {})'.format(self.rows, self.cols,
                                                  ', '.join(['({}, {}, {})'.format(k[0], k[1], v) for k, v in
                                                             self.matrix.items()]))

    def __getitem__(self, rc):
        self._validate_key(rc)
        return self.matrix.get(rc, 0)

    def __setitem__(self, rc, v):
        self._validate_key(rc)
        if type(v) is not int and type(v) is not float:
            raise TypeError('{} is not of int or float type'.format(v))
        if v == 0:
            if self.matrix.get(rc) is not None:
                del self.matrix[rc]
        else:
            self.matrix[rc] = v

    def __delitem__(self, rc):
        self._validate_key(rc)
        if rc in self.matrix:
            del self.matrix[rc]

    def _validate_key(self, key):
        if type(key) is not tuple or len(key) != 2:
            raise TypeError('{} is not a 2-tuple'.format(key))
        r, c = key
        if type(r) is not int or type(c) is not int:
            raise TypeError('{} is not an int 2-tuple'.format(key))
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            raise TypeError('{} is not legal'.format(key))

    def row(self, r):
        assert type(r) == int and 0 <= r < self.rows, 'Illegal row: {}'.format(r)
        return tuple(self.matrix.get((r, c), 0) for c in range(self.cols))

    def col(self, c):
        assert type(c) == int and 0 <= c < self.cols, 'Illegal column: {}'.format(c)
        return tuple(self.matrix.get((r, c), 0) for r in range(self.rows))

    def details(self):
        return '{}x{} -> {} -> {}'.format(self.rows, self.cols, self.matrix,
                                          tuple(tuple(self.matrix.get((r, c), 0)
                                                      for c in range(self.cols)) for r in range(self.rows)))

    # I've written str(...) because it is used in the bsc.txt file and
    # it is a bit subtle to get correct. This function does not depend
    # on any other method in this class being written correctly, although
    # it could be simplified by writing self[...] which calls __getitem__.
    def __str__(self):
        size = str(self.rows) + 'x' + str(self.cols)
        width = max(len(str(self.matrix.get((r, c), 0))) for c in range(self.cols) for r in range(self.rows))
        return size + ':[' + ('\n' + (2 + len(size)) * ' ').join('  '.join(
                '{num: >{width}}'.format(num=self.matrix.get((r, c), 0), width=width) for c in range(self.cols)) \
                                                                 for r in range(self.rows)) + ']'


if __name__ == '__main__':
    # Simple tests before running driver
    # print('Printing')
    # m = Sparse_Matrix(3, 3, (0, 0, 1), (1, 1, 3), (2, 2, 1))
    # print(m)
    # print(repr(m))
    # print(m.details())
    #
    # print('\nsize and len')
    # print(m.size(), len(m))
    #
    # print('\ngetitem and setitem')
    # print(m[1, 1])
    # m[1, 1] = 0
    # m[0, 1] = 2
    # print(m.details())
    #
    # print('\niterator')
    # for r, c, v in m:
    #     print((r, c), v)
    #
    # print('\nm, m+m, m+1, m==m, m==1')
    # print(m)
    # print(m + m)
    # print(m + 1)
    # print(m == m)
    # print(m == 1)
    # print()

    # driver tests
    import driver

    driver.default_file_name = 'bsc2.txt'
    # driver.default_show_exception = True
    # driver.default_show_exception_message = True
    # driver.default_show_traceback = True
    driver.driver()
