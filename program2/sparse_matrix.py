# Submitter: dparajul(Parajuli, Darshan)


class Sparse_Matrix:
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
    print('Printing')
    m = Sparse_Matrix(3, 3, (0, 0, 1), (1, 1, 3), (2, 2, 1))
    print(m)
    print(repr(m))
    print(m.details())

    print('\nsize and len')
    print(m.size(), len(m))

    print('\ngetitem and setitem')
    print(m[1, 1])
    m[1, 1] = 0
    m[0, 1] = 2
    print(m.details())

    print('\niterator')
    for r, c, v in m:
        print((r, c), v)

    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m + m)
    print(m + 1)
    print(m == m)
    print(m == 1)
    print()

    # driver tests
    import driver

    driver.default_file_name = 'bsc2.txt'
    #     driver.default_show_exception=True
    #     driver.default_show_exception_message=True
    #     driver.default_show_traceback=True
    driver.driver()
