'''
An Euler Cycle is a cycle in G that visits every edge exactly once.

The basic idea of this is that, for every vertex, the indegree should be equal to outdegree.

In the following code, an empty list is created, which will store the vertices or the path
of the cycle.

It starts from the begining of the graph and stores the vertice in the empty list.
It checks the edge of the current vertice and changes the current vertice to the edge.
By the end of the cycle, the path is stored in the list and displayed.
'''


graph = [(1, 2), (1, 4), (2, 3), (3, 1), (3, 4), (4, 3), (4, 1)]

def find_euler_cycle(graph):
  euler_cycle = []
  current = graph[0][0]
  euler_cycle.append (current)
  while len(graph) > 0:
    print (graph, current)
    for edge in graph:
      if current in edge:
        if edge[0] == current:
          current = edge[1]
        else:
          current = edge[0]
        graph.remove(edge)
        euler_cycle.append(current)
        break
    else:
      return False
  return euler_cycle

print(find_euler_cycle(graph))