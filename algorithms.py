import random

gnodes = dict()
ginfluences = dict()
selection = []

# Configs
INFLUENCE_DEPTH = 3

# Pega um nó randomico e realiza o climbing retornando o resultado
def climb(nodes):
    global gnodes
    gnodes = nodes

    # seleciona até 5 nós influentes em 10 tentativas
    while len(selection) < 5:
        actual_node = getRandomNode()

        # Climbing
        biggestNode = getBiggestNeighbor(actual_node)

        while actual_node != biggestNode:
            actual_node = biggestNode
            biggestNode = getBiggestNeighbor(actual_node)
        if biggestNode not in selection:
            selection.append(biggestNode)
    return selection

def getBiggestNeighbor(node):
    biggestInfluence = calculateInfluence(node)
    biggestNode = node
    for n in gnodes[node]:
        if n not in selection:
            if(calculateInfluence(n) > biggestInfluence):
                biggestInfluence = calculateInfluence(n)
                biggestNode = n
    return biggestNode


def getRandomNode():
    random_key = random.choice(list(gnodes.keys()))
    return random_key

# Calcula influencia até o 3 (INFLUENCE_DEPTH configurável) nível
def calculateInfluence(nodeKey):
    global ginfluences
    if nodeKey not in gnodes:
        return 1
    if nodeKey in ginfluences:
        return ginfluences[nodeKey]
    else:
        influenceCounter = set()
        nodesToSee = list()
        influenceCounter.add(nodeKey)
        nodesToSee.append(gnodes[nodeKey])
        for i in range(1, INFLUENCE_DEPTH):
            nextNodes = list()
            for n in nodesToSee:
                for vizinho in n:
                    if vizinho in influenceCounter:
                        pass
                    influenceCounter.add(vizinho)
                    if vizinho in gnodes:
                        nextNodes.append(gnodes[vizinho])
            nodesToSee = nextNodes
        ginfluences[nodeKey] = len(influenceCounter)
    return len(influenceCounter)