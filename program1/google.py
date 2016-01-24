from collections import defaultdict

import prompt


def all_prefixes(fq: (str,)) -> {(str,)}:
    return {fq[0:i + 1] for i in range(len(fq))}


def add_query(prefix: {(str,): {(str,)}}, query: {(str,): int}, new_query: (str,)) -> None:
    for i in range(len(new_query)):
        prefix[new_query[0:i + 1]].add(new_query)
    query[new_query] += 1


def read_queries(open_file: open) -> ({(str,): {(str,)}}, {(str,): int}):
    p, q = defaultdict(set), defaultdict(int)
    for line in open_file:
        line = line.rstrip('\n').split()
        add_query(p, q, tuple(line))
    return p, q


def dict_as_str(d: {None: None}, key: callable = None, reverse: bool = False) -> str:
    return ''.join(['  {} -> {}\n'.format(k, d[k]) for k in sorted(d.keys(), key=key, reverse=reverse)])


def top_n(a_prefix: (str,), n: int, prefix: {(str,): {(str,)}}, query: {(str,): int}) -> [(str,)]:
    return [k for k in sorted(prefix.get(a_prefix, []), key=lambda x: (-query[x], x)) if k in query][0:n]


# Script

if __name__ == '__main__':
    # Write script here
    p, q = None, None
    while True:
        name = prompt.for_string('Enter the name of a file with the full queries', is_legal=lambda x: len(x) > 0)
        try:
            with open(name, 'r') as file:
                p, q = read_queries(file)
            break
        except Exception as e:
            print(str(e))

    print()
    print('Prefix dictionary:')
    print(dict_as_str(p, key=lambda x: (len(x), x)))

    print()
    print('Query dictionary:')
    print(dict_as_str(q, key=lambda x: (-q[x], x)))

    while True:
        prefix = prompt.for_string('Enter a prefix (or quit)', is_legal=lambda x: len(x) > 0)
        if prefix == 'quit':
            break

        print()
        print('  Top 3 (at the most) full queries: {}'.format(top_n(tuple(prefix.split()), 3, p, q)))

        print()
        query = prompt.for_string('Enter a full query (or quit)', is_legal=lambda x: len(x) > 0)
        if query == 'quit':
            break

        add_query(p, q, tuple(query.split()))
        print()
        print('Prefix dictionary:')
        print(dict_as_str(p, key=lambda x: (len(x), x)))

        print()
        print('Query dictionary:')
        print(dict_as_str(q, key=lambda x: (-q[x], x)))

    # For running batch self-tests
    print()
    import driver

    driver.default_file_name = "bsc5.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
