# Não alcança todos os nós possíveis
def dfs_recursive_non_complete(graph, node, path, limit=4):
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


def dfs_recursive(graph, node, reached, curr_branch, visited_by_depth, limit):
    if node not in reached:
        reached += [node]
    curr_branch += [node]
    visited_by_depth[limit].append(node)
    # print('visiting', node)
    # print('branch:', curr_branch)
    limit -= 1
    # print('Limit is on', limit)

    # se chegar no limite permitido, não visita nenhum vizinho
    # do nó atual
    if limit > 0:
        if limit not in visited_by_depth.keys():
            visited_by_depth[limit] = []
        if node in graph.keys():
            for neighbor in graph[node]:
                if neighbor not in curr_branch and neighbor not in visited_by_depth[limit]:
                    # print(node, 'has Neighbor')
                    reached = dfs_recursive(graph, neighbor, reached, curr_branch, visited_by_depth, limit)
                    curr_branch.remove(neighbor)
    #             else:
    #                 print('Trying to visit a prev_node of current branch')
    #         print('End for', node)
    #     else:
    #         print(node, 'was a dead-end')
    # else:
    #     print('Limit reached')

    return reached


def assert_influence(graph, node_key, influence_value, limit=3):
    # dfs_recursive retorna os nós que visitou durante a busca por isso
    # o seu tamanho é igual ao alcance do nó, ou sua influência
    vbd = {limit: []}
    value = len(dfs_recursive(graph, node_key, [], [], vbd, limit))
    return [(value == influence_value), value]
