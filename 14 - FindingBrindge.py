
from collections import defaultdict

used = defaultdict(bool)
fup = []
tin = []
graph = {}
timer = 0
def dfs(graph, vertex):
    used[vertex] = True
    timer = timer + 1
    tin[vertex] = fup[vertex] = timer
    for i in graph[vertex]:
        if i == vertex:
            continue
        if used[i]:
            fup[vertex] = min(fup[vertex],tin[i])
        else:
            dfs(graph, i)
            fup[vertex] = min(fup[vertex],fup[i])
            if fup[i] > tin[vertex]:
                print("Bridge" + "i" + "vertex")


for i in graph.keys():
    if used[i] == False:
        dfs(graph,i)

