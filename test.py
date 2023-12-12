from collections import defaultdict, deque

# Function to build a graph from the input sequences
def build_graph(inputs):
    graph = defaultdict(list)

    for line in inputs:
        nums = line.split()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                graph[nums[i]].append(nums[j])
                graph[nums[j]].append(nums[i])

    return graph

# # Function to find the shortest path using BFS
# def shortest_path(graph, start, end):
#     if start == end:
#         return [start]

#     visited = {start}
#     queue = deque([(start, [])])

#     while queue:
#         node, path = queue.popleft()
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 new_path = path + [node, neighbor]
#                 if neighbor == end:
#                     return new_path + [end]
#                 queue.append((neighbor, new_path))

#     return None

# # Sample input data
# input_data = [
#     "1 2 3",
#     "2 3 4 5",
#     "4 5",
#     "1 2 3 4 5"
# ]

# # Build the graph
# graph = build_graph(input_data)

# # Find the shortest path
# start_node = input("Enter start node: ")
# end_node = input("Enter end node: ")

# path = shortest_path(graph, start_node, end_node)

# if path:
#     print("Shortest path:", " -> ".join(path))
# else:
#     print("No path found between the given nodes.")
