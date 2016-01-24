# Darshan Parajuli
# 16602518
# ICS 33

from collections import defaultdict

# Associates grades (str) with grade points (float)
UCI = {'A+': 4.0, 'A': 4.0, 'A-': 3.7,
       'B+': 3.3, 'B': 3.0, 'B-': 2.7,
       'C+': 2.3, 'C': 2.0, 'C-': 1.7,
       'D+': 1.3, 'D': 1.0, 'D-': 0.7,
       'F': 0.0}


def derivative(f: callable, delta: float) -> callable:
    if delta <= 0:
        raise AssertionError()
    return lambda x: (f(x + delta) - f(x)) / delta


def keys_with(d: {str: int}) -> callable:
    return lambda x: set([i for i in d.keys() if d[i] == x])


def flatten(db: {str: {(str, str)}}) -> [(str, str, str)]:
    return set([(x, a, b) for x in db.keys() for a, b in db[x]])


def roster(db: {str: {(str, str)}}) -> {str: [str]}:
    return {k: sorted([a for a, b in db[k]]) for k in db.keys()}


def averages(db: {str: {(str, str)}}) -> {str: float}:
    return {k: sum([UCI[b] for a, b in db[k]]) / len(db[k]) for k in db.keys()}


def grades1(db: {str: {(str, str)}}) -> {str: [(str, float)]}:
    return {k: sorted([(a, UCI[b]) for a, b in db[k]], key=lambda x: -x[1]) for k in db.keys()}


def grades2(db: {str: {(str, str)}}) -> {str: [str]}:
    return {k: [i for i, j in sorted([(a, UCI[b]) for a, b in db[k]], key=lambda x: (-x[1], x[0]))] for k in db.keys()}


def student_view(db: {str: {(str, str)}}) -> {str: {(str, str)}}:
    result = defaultdict(set)
    for k in db.keys():
        for a, b in db[k]:
            result[a].add((k, b))
    return dict(result)


def student_averages(db: {str: {(str, str)}}) -> {str: float}:
    result = {}
    for name in set([a for s in db.values() for a, b, in s]):
        if name not in result:
            grade_points = [UCI[j] for x in db.keys() for i, j in db[x] if i == name]
            result[name] = sum(grade_points) / len(grade_points)
    return result


if __name__ == '__main__':
    from goody import irange
    from math import log

    # Feel free to test other cases as well

    print('Testing derivative')
    d = derivative(lambda x: 3 * x ** 2 + 2 * x - 2, .000001)
    print([(a, d(a)) for a in irange(0, 10)])
    d = derivative(lambda x: log(x), .000001)  # derivative of log(x) is 1/x
    print([(a, d(a)) for a in irange(1, 10)])

    print('\nTesting keys_with')
    d = {'A': 3, 'B': 2, 'C': 3, 'D': 2, 'E': 2, 'F': 4, 'G': 1, 'H': 4}
    kw = keys_with(d)
    print([(x, kw(x)) for x in sorted(set(d.values()))])
    d = {'A': 1, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 8, 'G': 3, 'H': 6, 'I': 4, 'J': 1}
    kw = keys_with(d)
    print([(x, kw(x)) for x in sorted(set(d.values()))])

    print('\nTesting flatten')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(flatten(db))

    print('\nTesting roster')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(roster(db))

    print('\nTesting averages')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(averages(db))

    print('\nTesting grades1')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(grades1(db))

    print('\nTesting grades2')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B'), ('Zeke', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(grades2(db))

    print('\nTesting student_view')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(student_view(db))

    print('\nTesting student_averages')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
    print(student_averages(db))

    print('\ndriver testing with batch_self_check:')
    import driver

    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
