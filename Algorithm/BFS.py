from collections import deque

def BFS(graph, curr):
    # Store traversed order of visited nodes
    path = []

    # Track visited nodes
    visit = set()
    
    # Use a queue to determine which node to visit next
    queue = deque()
    queue.append(curr)
    while queue:
        curr = queue.popleft()
        if curr not in visit:
            visit.add(curr)
            path.append(curr)

            for neighbor in graph[curr]:
                if neighbor not in visit:
                    queue.append(neighbor)

    return path


if __name__=="__main__":
    # Graph with the 'index' as the node and its 'value' as the neighbors
    edgeList = [
        [1, 3],
        [2],
        [],
        [4, 6, 7],
        [2, 5],
        [2],
        [],
        []
    ]

    print(BFS(edgeList, 0))

    # Graph with the 'key' as the node and 'value' as the neighbors
    adjacencyList = {
        0: [1, 3],
        1: [2],
        2: [],
        3: [4, 6, 7],
        4: [2, 5],
        5: [2],
        6: [],
        7: []
    }

    print(BFS(adjacencyList, 0))