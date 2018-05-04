import re
# Carrega os dados para uma estrutura de lista de lista de relaionamentos
# e carrega as features para um hashmap (para o propósito desse trablaho
# o arquivo circles e todas as referências aos dados contidos nele serão ignorados)

edge_file = open("twitter/12831.edges", "r")
edges = dict()
for edge_line in edge_file:
    reg = re.search("(\w+) (\w+)",edge_line)
    if reg.group(1) not in edges:
        edges[reg.group(1)] = [reg.group(2)]
    else:
        edges[reg.group(1)].append(reg.group(2))

print(edges)