import random

gnodes = dict()
ginfluences = dict()

# Configs
INFLUENCE_DEPTH = 3

# Pega um nó randomico e realiza o climbing retornando o resultado
# TODO talvez seja melhor realizar umas 5 ou 10 vezes e retornar todos os resultados
def climb(nodes):
    global gnodes
    gnodes = nodes
    first_node = getRandomNode()
    print(calculateInfluence(first_node))
    print(first_node)
    print(gnodes[first_node])


def getRandomNode():
    random_key = random.choice(list(gnodes.keys()))
    return random_key

# Calcula influencia até o 3 (INFLUENCE_DEPTH configurável) nível
def calculateInfluence(nodeKey):
    global ginfluences
    if nodeKey in ginfluences:
        return ginfluences[node.keys()[0]]
    else:
        influenceCounter = set()
        nodesToSee = list()
        influenceCounter.add(nodeKey)
        nodesToSee.append(gnodes[nodeKey])
        for i in range(0, INFLUENCE_DEPTH):
            nextNodes = list()
            for n in nodesToSee:
                for vizinho in n:
                    if vizinho in influenceCounter:
                        pass
                    influenceCounter.add(vizinho)
                    if vizinho in gnodes:
                        nextNodes.append(gnodes[vizinho])
            nodesToSee = nextNodes
    return len(influenceCounter)