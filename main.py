import functions
import algorithms
import busca
import datetime
# Carrega os dados para uma estrutura de lista de lista de relacionamentos
# e carrega as features para um hashmap (para o propósito desse trabalho
# o arquivo circles e todas as referências aos dados contidos nele serão ignorados)

edges = functions.carrega_edges()
#features = functions.carrega_features()

algorithms.carregaNos(edges)
pre = datetime.datetime.now()
selection = algorithms.climb(edges)
pos = datetime.datetime.now()
print("Resultado da Heurística:")
print(" Climbing demora: "+ str(pos-pre))
print(" Qtd de nós vizitados: " + str(len(algorithms.ginfluences)))
count = 0
for n in selection:
    count += 1
    print(" "+str(count)+"# Nó escolhido:", n,
          "- com infuência de", algorithms.calculateInfluence(n))

# print(features['35415466'])

# Busca em profundidade com limitador
print("|-------------------------------------------------------------------------|")
print("Verificação do resultado utilizando busca em profundidade:")
count = 0
for n in selection:
    count += 1
    pre = datetime.datetime.now()
    result = busca.assert_influence(edges, n, algorithms.calculateInfluence(n))
    if result[0]:
        print(' ' + str(count) + '# Nó', n, ': valor de infuência corresponde')
    else:
        print(' ' + str(count) + '# Nó', n, ': valor de influência não corresponde. Busca retornou:',
              result[1])
    pos = datetime.datetime.now()
    print('    verificação demorou: ' + str(pos - pre))
