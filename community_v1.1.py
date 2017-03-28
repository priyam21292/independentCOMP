'''
Identify communities in a random undirected graph

	- Take user input for number of vertices, p-value and density
	- Generate a random-graph using the user input
	- Generate all the possible subgraphs of the graph
	- For each subset, check if it's density id greater than threshold density
'''
import graph 
import itertools
from math import factorial

# Take user inputs
V = int(input ("Enter No. of Vertices: ") )
p = float(input ("Enter p-value: ") )
threshold = float(input ("Enter threshold density: ") )

# Create a random-graph using the input
G = graph.random_graph(V,p)

def max_edge(n):
	return factorial(n) / factorial(2) / factorial(n-2)

community = []
min_edges = 0
for i in range(V,2):
	min_edges = threshold * max_edge(i)
	print (i)
	for j in range(min_edges, max_edge):
		possible_combinations = list(itertools.combinations(range(i),j))
		for x in possible_combinations:
			for f in possible_combinations[j]:
				if (possible_combinations[x][j], possible_combinations[x][f+1]) in G:
					pass
				else:
					continue
			community.append(x)				


density = 2.0*len(G._edges)/(V*(V-1))
print (density)
print (community)




'''
To get the subsets, I was applying the following logic - 
	- The number of minimum edges can be determined by the given threshold and the maximum number of possible edges.
	- Iterate from min_edges to max_edges because they will be above the threshold and find all the possible combinations.
	- Check all the combinations and if all the sibsets are in the graph, store it in a new list.
'''


