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
print (G._edges)

def max_edge(n):
	m_edge = int(factorial(n) / factorial(2) / factorial(n-2))
	return m_edge

community = []
min_edges = 0
for i in range(V, 2, -1):
	min_edges = int(threshold * max_edge(i))
	for j in range(min_edges, max_edge(i)):
		possible_combinations = list(itertools.combinations(range(i),j))
		for x in range(0,len(possible_combinations)-1):
			temp = []
			temp1 = 1
			for f in range(0,len(possible_combinations[x])-1):
				#print f
				if (possible_combinations[x][f], possible_combinations[x][f+1]) in G:
					temp.insert(possible_combinations[x][f], possible_combinations[x][f+1])
				else:
					continue
			if len(temp) == len (possible_combinations[x]):
				community.insert(temp1)		



density = 2.0*len(G._edges)/(V*(V-1))
print (density)
print (community)
print (temp)



'''
To get the subsets, I was applying the following logic - 
	- Loop through each vertice
	- Start with the first vertice, and explore the neighbours.
	### I tried to do this using G.out_neighbours but got an attribute error.
	- If the neighbours are connected by an edge, there is a cycle or a subgraph.
	- Store each subgraph in a list.

To check for the subsets that qualify as a community given the threshold - 
	- Iterate through the list and check for the number of vertices (V) and number of edges (E)
	- Apply the formula 2 * E/ (V*(V-1))
	- If the value is greater than the threshold, print the subset.
'''


