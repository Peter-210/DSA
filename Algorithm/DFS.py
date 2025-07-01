def DFSRecursion(graph, curr):
    # Store traversed order of visited nodes
    path = []

    # Track visited nodes
    visit = set()

    # Use recursion to traverse through the graph
    def recursive(graph, curr, visit):
        path.append(curr)
        visit.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visit:
                recursive(graph, neighbor, visit)

    recursive(graph, curr, visit)
    return path


def DFSStack(graph, curr):
    # Store traversed order of visited nodes
    path = []

    # Track visited nodes
    visit = set()
    
    # Use a stack to determine which node to visit next
    stack = [curr]
    while stack:
        curr = stack.pop()
        if curr not in visit:
            visit.add(curr)
            path.append(curr)

            for neighbor in graph[curr]:
                if neighbor not in visit:
                    stack.append(neighbor)

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

    print(DFSStack(edgeList, 0))
    print(DFSRecursion(edgeList, 0))

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

    print(DFSStack(adjacencyList, 0))
    print(DFSRecursion(adjacencyList, 0))