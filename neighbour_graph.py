'''
A simple code to display the neighbours.
'''

graph = { "a" : ["c", "d", "f"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c", "e"],
          "e" : ["c", "b". "d"],
          "f" : []
        }

def gen_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

print(gen_edges(graph))