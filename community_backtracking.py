import graph
from math import factorial		# To calculate the maximum number of possible edges

# Take the user inputs
N = int(input ("Enter No. of Vertices: ") )		# No. of Vertices
p = float(input ("Enter p-value: ") )	# p-value to generate the edges
threshold = float(input ("Enter threshold density: ") )		# Threshold to get communities

G = graph.random_graph(N,p)		# Generate a random graph based on input
Solution = [-1]*N 		# Solution array with size N
result = []

# max_edge returns the maximum number of edges possible with the given no. of vertices
def max_edge(n):
	m_edge = int(factorial(n) / factorial(2) / factorial(n-2))
	return m_edge

# ActualSet returns the actual set of vertices
def ActualSet(s):
	return [ i for i in range(len(s)) if s[i] == True]

def Community(i):
	if promising(i):
		if i==N-1:
			if len(ActualSet(Solution)) > 3:
				# check if the density is above the threshold
				if len(ActualSet(Solution))/max_edge(len(ActualSet(Solution))) > threshold:
					result.append(ActualSet(Solution))
		else:
			Solution[i+1] = False	
			Community(i+1)
			Solution[i+1] = True
			Community(i+1)

def promising(i):
	if i<N-1:
		return True
	for j in range(N):
		for k in range(j+1, N):
			# if Solution j and k are True but not in Graph
			if j!=k and Solution[k] == True and Solution[j] == True and (j,k) not in G:
				return False
	return True

Community(-1)
print(result)		# print the communities
print (len(result))	# print total number of communities


''' 
C:\Users\Priyam\Desktop\BioinfoAlgo>python community_backtracking.py 
Enter No. of Vertices: 20 
Enter p-value: 0.5 
Enter threshold density: 0.5 
[[15, 16, 17, 19], [13, 15, 17, 18], [13, 15, 16, 17], [12, 16, 17, 19], [12, 13, 16, 17],
[9, 13, 15, 18], [9, 13, 15, 16], [9, 12, 13, 16], [9, 11, 15, 18], [9, 10, 12,
13], [9, 10, 11, 12], [7, 9, 13, 16], [7, 8, 14, 16], [6, 15, 16, 17], [6, 13,
16, 17], [6, 13, 15, 17], [6, 13, 15, 16], [6, 12, 16, 17], [6, 12, 13, 17], [6,
12, 13, 16], [6, 9, 15, 16], [6, 9, 13, 16], [6, 9, 13, 15], [6, 9, 12, 16], [6,
9, 12, 13], [6, 9, 11, 15], [6, 9, 11, 12], [6, 7, 13, 16], [6, 7, 9, 16], [6,
7, 9, 13], [6, 7, 9, 11], [6, 7, 8, 16], [5, 12, 16, 17], [5, 9, 12, 16], [5, 9,
11, 18], [5, 9, 11, 12], [5, 6, 16, 17], [5, 6, 12, 17], [5, 6, 12, 16], [5, 6,
11, 12], [5, 6, 9, 16], [5, 6, 9, 12], [5, 6, 9, 11], [4, 15, 17, 18], [4, 13,
17, 18], [4, 13, 15, 18], [4, 13, 15, 17], [4, 12, 13, 17], [4, 9, 15, 18], [4,
9, 13, 18], [4, 9, 13, 15], [4, 9, 12, 13], [4, 7, 9, 13], [4, 6, 15, 17], [4,
6, 13, 17], [4, 6, 13, 15], [4, 6, 12, 17], [4, 6, 12, 13], [4, 6, 9, 15], [4,
6, 9, 13], [4, 6, 9, 12], [4, 6, 7, 13], [4, 6, 7, 9], [4, 6, 7, 8], [3, 16, 17,
19], [3, 13, 16, 17], [3, 12, 17, 19], [3, 12, 16, 19], [3, 12, 16, 17], [3, 12,
13, 17], [3, 12, 13, 16], [3, 9, 13, 16], [3, 9, 12, 16], [3, 9, 12, 13], [3, 9,
11, 12], [3, 8, 14, 16], [3, 7, 16, 19], [3, 7, 14, 16], [3, 7, 13, 16], [3, 7,
11, 14], [3, 7, 9, 16], [3, 7, 9, 13], [3, 7, 9, 11], [3, 7, 8, 16], [3, 7, 8,
14], [3, 6, 16, 17], [3, 6, 13, 17], [3, 6, 13, 16], [3, 6, 12, 17], [3, 6, 12,
16], [3, 6, 12, 13], [3, 6, 11, 12], [3, 6, 9, 16], [3, 6, 9, 13], [3, 6, 9,
12], [3, 6, 9, 11], [3, 6, 8, 16], [3, 6, 7, 16], [3, 6, 7, 13], [3, 6, 7, 11],
[3, 6, 7, 9], [3, 6, 7, 8], [2, 15, 16, 19], [2, 12, 16, 19], [2, 10, 12, 19],
[2, 7, 16, 19], [2, 3, 16, 19], [2, 3, 12, 19], [2, 3, 12, 16], [2, 3, 7, 19],
[2, 3, 7, 16], [1, 13, 17, 18], [1, 12, 17, 19], [1, 12, 13, 17], [1, 10, 12,
19], [1, 10, 12, 13], [1, 10, 11, 12], [1, 5, 17, 18], [1, 5, 12, 17], [1, 5,
11, 18], [1, 5, 11, 12], [1, 4, 17, 18], [1, 4, 13, 18], [1, 4, 13, 17], [1, 4,
12, 17], [1, 4, 12, 13], [1, 3, 17, 19], [1, 3, 13, 17], [1, 3, 12, 19], [1, 3,
12, 17], [1, 3, 12, 13], [1, 3, 11, 14], [1, 3, 11, 12], [1, 3, 8, 14], [1, 2,
12, 19], [1, 2, 10, 19], [1, 2, 10, 12], [1, 2, 3, 19], [1, 2, 3, 12], [0, 12,
16, 19], [0, 9, 12, 16], [0, 4, 9, 12]]  
142

C:\Users\Priyam\Desktop\BioinfoAlgo>python community_backtracking.py Enter No.
of Vertices: 20 Enter p-value: 0.4 Enter threshold density: 0.5 [[7, 11, 16,
17], [5, 10, 11, 17], [4, 11, 16, 17], [4, 11, 13, 17], [4, 7, 16, 17], [4, 7,
11, 17], [4, 7, 11, 16], [4, 7, 9, 17], [4, 7, 8, 18], [4, 7, 8, 16], [4, 5, 11,
17], [2, 7, 8, 16], [0, 7, 11, 16], [0, 7, 8, 18], [0, 7, 8, 16]] 15

'''