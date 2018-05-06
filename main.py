import functions
import algorithms
import busca
import datetime
# Carrega os dados para uma estrutura de lista de lista de relaionamentos
# e carrega as features para um hashmap (para o propósito desse trablaho
# o arquivo circles e todas as referências aos dados contidos nele serão ignorados)

edges = functions.carrega_edges()
#features = functions.carrega_features()

pre = datetime.datetime.now()
node = algorithms.climb(edges)
pos = datetime.datetime.now()
print("Climbing demora: "+ str(pos-pre))
print("Qtd de nós vizitados: " + str(len(algorithms.ginfluences)))
print(algorithms.calculateInfluence(node))
#print(features['35415466'])

# Exemplo de assert usando a busca
## Heurítica achou que o nó '12831' é um influenciador com uma influencia de 237
if busca.assert_influence(edges, '12831', 237):
    print('12831 de fato influencia 237')
else:
    print('12831 não influencia 237')
