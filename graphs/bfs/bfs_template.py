# initialize the visited array of size n
visited = [-1] * n

q = collections.deque([source])
visited[source] = 1

while len(q) != 0:
    node = q.popleft()
    for neighbor in adjlist[node]:
        if visited[neighbor] == -1:
            visited[neighbor] = 1
            q.append(neighbor)
