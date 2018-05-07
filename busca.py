def dfs_recursive(graph, node, path, limit=4):
    path += [node]
    # print('visiting', node)
    limit -= 1
    # print('Limit is on', limit)

    # se chegar no limite permitido, não visita nenhum vizinho
    # do nó atual
    if limit > 0:
        if node in graph.keys():
            for neighbor in graph[node]:
                if neighbor not in path:
                    # print(node, 'is Parent')
                    path = dfs_recursive(graph, neighbor, path, limit)
    #         print('End for', node)
    #     else:
    #         print(node, 'was a dead-end')
    # else:
    #     print('Limit reached')

    return path


def assert_influence(graph, node_key, influence_value):
    # dfs_recursive retorna os nós que visitou durante a busca por isso
    # o seu tamanho é igual ao alcance do nó, ou sua influência
    value = dfs_recursive(graph, node_key, path=[]).__len__()
    return [(value == influence_value), value]
