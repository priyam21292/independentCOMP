'''
- Take a sample distance matrix with values ranging from 0,1
- From the distance matrix, find the closest clusters (i.e minimum distance)
- Merge the closest clusters and update the distance matrix, depending on the linkage method (average, single and complete)
	- For this example we will use the complete linkage
	- In complete linkage, the matrix will be updated based on the Maximum Distance of the pairs
- Repeat this until (n-1) times
'''

# Pseudo Code
'''
Hierarchical(d,n) 		# d as the input matrix
	n clusters with one element
	while more than 1 cluster
		find closest clusters
		merge closest clusters
		remove the rows and columns corresponding to new cluster
		recalculate distance
'''
