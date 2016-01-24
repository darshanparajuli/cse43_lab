from collections import defaultdict

import prompt


def read_ndfa(file: open) -> {str: {str: {str}}}:
    ndfa = {}
    for line in file:
        line = line.rstrip('\n').split(';')
        inner = defaultdict(set)
        rest = line[1:]
        for i in range(0, len(rest), 2):
            inner[rest[i]].add(rest[i + 1])
        ndfa[line[0]] = dict(inner)
    return ndfa


def ndfa_as_str(ndfa: {str: {str: {str}}}) -> str:
    return ''.join(['  {} transitions: {}\n'.format(k, [(i, sorted(ndfa[k][i])) for i in sorted(ndfa[k].keys())])
                    for k in sorted(ndfa.keys())])


def process(ndfa: {str: {str: {str}}}, state: str, inputs: [str]) -> [None]:
    result = [state]
    states = {state}
    for i in inputs:
        next_states = set()
        for s in states:
            if i in ndfa[s]:
                next_states.update(ndfa[s][i])
        result.append((i, next_states))
        if len(next_states) == 0:
            break
        states = next_states
    return result


def interpret(ndfa_result: [None]) -> str:
    result = 'Start state = {}\n'.format(ndfa_result[0])
    stop_state = {}
    for i, s in ndfa_result[1:]:
        result += '  Input = {}; new possible states = {}\n'.format(i, sorted(s))
        stop_state = s
    result += 'Stop state(s) = {}\n'.format(sorted(stop_state))
    return result


if __name__ == '__main__':
    # Write script here
    ndfa = None
    while True:
        name = prompt.for_string('Enter the name of a file with a non-deterministic finite automaton',
                                 is_legal=lambda x: len(x) > 0)
        try:
            with open(name, 'r') as file:
                ndfa = read_ndfa(file)
            break
        except Exception as e:
            print(str(e))

    print()
    print('Non-Deterministic Finite Automaton')
    print(ndfa_as_str(ndfa))

    while True:
        name = prompt.for_string('Enter the name of a file with the start-state and input',
                                 is_legal=lambda x: len(x) > 0)
        try:
            with open(name, 'r') as file:
                print()
                for line in file:
                    line = line.rstrip('\n').split(';')
                    result = process(ndfa, line[0], line[1:])
                    print(interpret(result))
            break
        except Exception as e:
            print(str(e))

    # For running batch self-tests
    print()
    import driver

    driver.default_file_name = "bsc4.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
