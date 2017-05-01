import graph

# Take the user inputs
N = int(input ("Enter No. of Vertices: ") )		# No. of Vertices
p = float(input ("Enter p-value: ") )	# p-value to generate the edges
threshold = float(input ("Enter threshold density: ") )		# Threshold to get communities

G = graph.random_graph(N,p)		# Generate a random graph based on input
Solution = [-1]*N 		# Solution array with size N
result = []			# To store the list of communities

# ActualSet returns the actual set of vertices
def ActualSet(s):
	return [ i for i in range(len(s)) if s[i] == 1]

def Community(i):
	if promising(i):
		if i==N-1:
			result.append(ActualSet(Solution))
		else:
			Solution[i+1] = 0	
			Community(i+1)
			Solution[i+1] = 1
			Community(i+1)

def promising(i):
	count = 0		# To count the number of edges in the current subset (used in calculating the density)
	max_edges = 0	# To get the maximum number of possible edges possible with current subset
	# V*(V-1)/2
	max_edges = int(len(ActualSet(Solution))*(len(ActualSet(Solution))-1)/2)
	if i<N-1:
		return True
	else:
		if len(ActualSet(Solution)) <= 2:
			return False
		else:
			for e in G.Edges:
				u, v = e[0], e[1]
				if Solution[u] == 1 and Solution[v] == 1:
					count = count+1		# Increment of count if there is an edge
					if (count/max_edges) > threshold: 	# if density greater than threshold
						return True
			return False

Community(-1)
print(result)		# Print the communities
print ("\nNumber of Communities:",len(result))	# Print total number of communities