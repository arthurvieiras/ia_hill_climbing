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