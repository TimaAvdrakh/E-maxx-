graph = {}

## doing some input to graph
weight = [100000000]*graph.__len__()

rebra = {}

## inputing some rebra

def BFShort(graph):
    for i in graph:
        for j in i:
            weight[j] = min(weight[j],weight[i]+rebra[i][j])

for i in range(len(graph)-1):
    BFShort(graph)

