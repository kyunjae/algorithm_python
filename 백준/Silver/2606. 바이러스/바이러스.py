n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)


dfs(1)
print(sum(visited)-1)
