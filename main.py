import functions
import algorithms
import busca
import datetime
# Carrega os dados para uma estrutura de lista de lista de relacionamentos
# e carrega as features para um hashmap (para o propósito desse trabalho
# o arquivo circles e todas as referências aos dados contidos nele serão ignorados)

edges = functions.carrega_edges()
#features = functions.carrega_features()

pre = datetime.datetime.now()
selection = algorithms.climb(edges)
pos = datetime.datetime.now()
print("Resultado da Heurística:")
print(" Climbing demora: "+ str(pos-pre))
print(" Qtd de nós vizitados: " + str(len(algorithms.ginfluences)))
count = 0
for n in selection:
    count += 1
    print(" ", count, "# Nó escolhido:", n)
    print(" Valor de infuencia do nó:", algorithms.calculateInfluence(n))
#print(features['35415466'])

# Exemplo de assert usando a busca
## Heurítica achou que o nó '12831' é um influenciador com uma influencia de 237
print("----------------------------")
print("Verificação utilizando busca em profundidade:")
count = 0
for n in selection:
    count += 1
    result = busca.assert_influence(edges, n, algorithms.calculateInfluence(n))
    if result[0]:
        print(' #', count, 'Nó', n, ': valor de infuência verificado')
    else:
        print(' #', count, 'Nó', n, ': valor de influência não corresponde. Busca retornou:',
              result[1])
