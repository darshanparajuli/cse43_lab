import prompt


def read_fa(file: open) -> {str: {str: str}}:
    fa = {}
    for line in file:
        line = line.rstrip('\n').split(';')
        fa[line[0]] = dict(zip(line[1::2], line[2::2]))
    return fa


def fa_as_str(fa: {str: {str: str}}) -> str:
    return ''.join(['  {} transitions: {}\n'.format(k, [(i, fa[k][i]) for i in sorted(fa[k].keys())])
                    for k in sorted(fa.keys())])


def process(fa: {str: {str: str}}, state: str, inputs: [str]) -> [None]:
    result = [state]
    for i in inputs:
        state = fa[state].get(i, None)
        result.append((i, state))
        if state is None:
            break
    return result


def interpret(fa_result: [None]) -> str:
    result = 'Start state = {}\n'.format(fa_result[0])
    stop_state = None
    for i, s in fa_result[1:]:
        result += '  Input = {}; '.format(i)
        if i == 'x':
            result += 'illegal input: simulation terminated\n'
        else:
            result += 'new state = {}\n'.format(s)
        stop_state = s
    result += 'Stop state = {}\n'.format(stop_state)
    return result


if __name__ == '__main__':
    # Write script here
    fa = None
    while True:
        name = prompt.for_string('Enter the name of a file with a finite automaton', is_legal=lambda x: len(x) > 0)
        try:
            with open(name, 'r') as file:
                fa = read_fa(file)
            break
        except Exception as e:
            print(str(e))

    print()
    print('Finite Automation')
    print(fa_as_str(fa))

    while True:
        name = prompt.for_string('Enter the name of a file with the start-state and input',
                                 is_legal=lambda x: len(x) > 0)
        try:
            with open(name, 'r') as file:
                print()
                for line in file:
                    line = line.rstrip('\n').split(';')
                    result = process(fa, line[0], line[1:])
                    print(interpret(result))
            break
        except Exception as e:
            print(str(e))

    # For running batch self-tests
    print()
    import driver

    driver.default_file_name = "bsc3.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
