'''
	UUG is a simple unweighted, undirected graph data structure
	for the purpose of testing graph algorithms.

	Usage:
	G = Graph()
	G.add(2,3)       						# add edge (2,3)
	G.add(3,5)       						# add edge (3,5)
	G.add(3,10)      						# add edge (3,10)
	print( (3,5) in G )					# should be True
	print( (5,3) in G )					# should be True
	print( (10,5) in G )				# should be False
	print( (1,5) in G )					# should be False
	print( "All vertices:", G.vertices )
	print( "All edges:", G._edges )
	print( "Neighbor of vertex 3:", G.neighbors[3] )
	
'''
import random
INFINITY = float("inf")

def random_graph(n,p,seed=None):
	random.seed(seed)
	g = Graph()
	for i in range(n):
		for j in range(i+1,n):
			if random.random() < p and i!=j:
				g.add(i,j)
	return g

class Node(object):
	def __init__(self, id):
		self.id = id

class Graph(object):
	def __init__(self, *vertex_attrs):
		self._edges = {}
		self.vertices = {}
		self.neighbors = {}
		self.vertex_attrs = vertex_attrs

	def add_vertex(self, i):
		if i not in self.vertices:
			self.vertices[i] = Node(i)
			for a in self.vertex_attrs:
				setattr(self.vertices[i], a, None)
			self.neighbors[i] = set()

	def delete_vertex(self, i):
		if i in self.vertices:
			del self.vertices[i]
			for j in self.neighbors[i]:
				del self._edges[i,j]
				del self._edges[j,i]
				self.neighbors[j].remove(i)
			del self.neighbors[i]
		
	def add(self, i,j, w=None):
		self._edges[i,j] = w
		self.add_vertex(i)
		self.neighbors[i].add(j)
		self._edges[j,i] = w
		self.add_vertex(j)
		self.neighbors[j].add(i)

	def __getitem__(self, thing):
		if isinstance(thing, tuple):
			if thing not in self._edges:
				return None
			return self._edges[thing]
		else:
			if thing not in self.vertices:
				return None
			return self.vertices[thing]

	def __contains__(self, thing):
		if isinstance(thing, int):
			return thing in self.vertices
		else:
			return thing in self._edges


class DGraph(object):
	def __init__(self, *vertex_attrs):
		self._edges = {}
		self.vertices = {}
		self.in_neighbors = {}
		self.out_neighbors = {}
		self.vertex_attrs = vertex_attrs

	def add_vertex(self, i):
		if i not in self.vertices:
			self.vertices[i] = Node(i)
			for a in self.vertex_attrs:
				setattr(self.vertices[i], a, None)
			self.out_neighbors[i] = set()
			self.in_neighbors[i] = set()

	def delete_vertex(self, i):
		if i in self.vertices:
			del self.vertices[i]
			OUT = [j for j in self.out_neighbors[i]]
			for j in OUT:
				del self._edges[i,j]
				self.out_neighbors[i].remove(j)
				self.in_neighbors[j].remove(i)
			del self.out_neighbors[i]
			IN = [j for j in self.in_neighbors[i]]
			for j in IN:
				del self._edges[j,i]
				self.out_neighbors[j].remove(i)
			del self.in_neighbors[i]
			
	def add(self, i,j, w=None):
		self._edges[i,j] = w
		self.add_vertex(i)
		self.out_neighbors[i].add(j)
		self.add_vertex(j)
		self.in_neighbors[j].add(i)

	def __getitem__(self, thing):
		if isinstance(thing, tuple):
			if thing not in self._edges:
				return None
			return self._edges[thing]
		else:
			if thing not in self.vertices:
				return None
			return self.vertices[thing]

	def __contains__(self, thing):
		if isinstance(thing, int):
			return thing in self.vertices
		else:
			return thing in self._edges



if __name__ == '__main__':
	G = Graph()
	G.add(2,3)       						# add edge (2,3)
	G.add(3,5)       						# add edge (3,5)
	G.add(3,10)      						# add edge (3,10)
	print( (3,5) in G )					# should be True
	print( (5,3) in G )					# should be True
	print( (10,5) in G )				# should be False
	print( (1,5) in G )					# should be False
	print( "All vertices:", G.vertices )
	print( "All edges:", G._edges )
	print( "Neighbor of vertex 3:", G.neighbors[3] )