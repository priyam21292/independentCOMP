'''
Identify communities in a random undirected graph

	- Take user input for number of vertices, p-value and density
	- Generate a random-graph using the user input
	- Generate all the possible subgraphs of the graph
	- For each subset, check if it's density id greater than threshold density
'''
import graph 

# Take user inputs
V = int(input ("Enter No. of Vertices: ") )
p = float(input ("Enter p-value: ") )
threshold = float(input ("Enter threshold density: ") )

# Create a random-graph using the input
G = graph.random_graph(V,p)
print (G._edges)

print(G.neighbours[2])

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


