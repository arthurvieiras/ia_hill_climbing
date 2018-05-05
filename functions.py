import re
import glob

def carrega_edges():
    edges = dict()
    for file_name in glob.glob("twitter/*.edges"):
        edge_file = open(file_name, "r")
        edges[re.search("(\w+).edges",file_name).group(1)] = set()
        for edge_line in edge_file:
            reg = re.search("(\w+) (\w+)",edge_line)
            if reg.group(1) not in edges:
                edges[reg.group(1)] = set([reg.group(2)])
            else:
                edges[reg.group(1)].add(reg.group(2))
            edges[re.search("(\w+).edges",file_name).group(1)].add(reg.group(1))
            edges[re.search("(\w+).edges",file_name).group(1)].add(reg.group(2))
    return edges

# TODO Falta colocar as features do ego node, adicionar o quanto antes #facil
def carrega_features():
    feats = dict()
    feat_names = []
    for file_name in glob.glob("twitter/*.feat"):
        feat_file = open(file_name, "r")
        egoID = re.search("(\w+).feat",file_name).group(1)
        feat_name_file = open("twitter/"+egoID+".featnames", encoding="utf8")
        ego_feat_file = open("twitter/"+egoID+".egofeat")
        # Captura nome das features
        for feat_name_line in feat_name_file:
            reg = re.search("(\d) (.*)",feat_name_line)
            feat_names.append(reg.group(2))
        # Pega os valores das features para cada nó
        for feat_line in feat_file:
            reg = re.search("(\w+) (.*)",feat_line)
            for idx, value in enumerate(reg.group(2).split(" ")):
                if reg.group(1) not in feats:
                    feats[reg.group(1)] = dict()
                feats[reg.group(1)][feat_names[idx]] = value
        # Adiciona valor das features para o egonode
        feat_line = ego_feat_file.readline()
        for idx, value in enumerate(feat_line.split(" ")):
            if egoID not in feats:
                feats[egoID] = dict()
            feats[egoID][feat_names[idx]] = value
    return feats