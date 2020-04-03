from collections import defaultdict

used = defaultdict(bool)
graph = {}

ans = []

def dfs(graph, vertex):
    used[vertex] == True
    for i in graph[vertex]:
        if used[i] == False:
            dfs(graph, i)
    ans.append(vertex)

for i in graph.keys():
    if used[i] == False:
        dfs(i)

ans = ans.reverse()

