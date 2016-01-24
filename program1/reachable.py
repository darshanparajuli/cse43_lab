from collections import defaultdict

import prompt


def read_graph(file: open) -> {str: {str}}:
    graph = defaultdict(set)
    for line in file:
        line = line.rstrip('\n').split(';')
        graph[line[0]].add(line[1])
    return dict(graph)


def graph_as_str(graph: {str: {str}}) -> str:
    return ''.join(['  {0} -> {1}\n'.format(k, str(sorted(graph[k]))) for k in sorted(graph.keys())])


def reachable(graph: {str: {str}}, start: str) -> {str}:
    reached_nodes = set()
    explored_nodes = [start]

    while explored_nodes:
        node = explored_nodes.pop()
        reached_nodes.add(node)
        if graph.get(node):
            for n in graph[node]:
                if n not in reached_nodes:
                    explored_nodes.append(n)

    return reached_nodes


if __name__ == '__main__':
    # Write script here
    graph = None
    while True:
        name = prompt.for_string('Enter the name of a file with a graph', is_legal=lambda x: len(x) > 0)
        try:
            file = open(name, 'r')
        except Exception as e:
            print(str(e))
        else:
            try:
                graph = read_graph(file)
                if len(graph):
                    break
                else:
                    raise Exception()
            except:
                print(name, 'does not have a valid graph')
            finally:
                file.close()

    print('{}\n{}'.format('Graph: source -> {destination} edges', graph_as_str(graph)))

    while True:
        user_input = prompt.for_string('Enter the name of a starting node',
                                       is_legal=lambda x: graph.get(x) or x == 'quit',
                                       error_message='Illegal: not a source node')
        if user_input == 'quit':
            break

        print('From {} the reachable nodes are {}'.format(user_input, graph[user_input]))

    # For running batch self-tests
    print()
    import driver

    driver.default_file_name = "bsc1.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
