def dfs_recursive(graph, vertex, path=[], limit=4):
    path += [vertex]
    # print('visiting', vertex)
    limit -= 1
    # print('Limit is on', limit)

    if limit > 0:
        if vertex in graph.keys():
            for neighbor in graph[vertex]:
                if neighbor not in path:
                    # print(vertex, 'is Parent')
                    path = dfs_recursive(graph, neighbor, path, limit)
    #         print('End for', vertex)
    #     else:
    #         print(vertex, 'was Leaf')
    # else:
    #     print('Limit reached')

    return path


def assert_influence(graph, node_key, influence_value):
    value = dfs_recursive(graph, node_key).__len__()
    return value == influence_value
