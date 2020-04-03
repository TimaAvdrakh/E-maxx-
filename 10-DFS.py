def dfs(graph, s):
    visited = []
    path = []
    visited[s] = True
    for i in graph[s]:
        if(visited[i]!=True):
            path.append(graph[i])
            dfs(i)
    return path

