import functions
import algorithms
# Carrega os dados para uma estrutura de lista de lista de relaionamentos
# e carrega as features para um hashmap (para o propósito desse trablaho
# o arquivo circles e todas as referências aos dados contidos nele serão ignorados)

edges = functions.carrega_edges()
#features = functions.carrega_features()

algorithms.climb(edges)
#print(features['35415466'])