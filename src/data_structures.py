import numpy as np


class Vertex:
	
	def __init__(self, idx):
		self.idx = idx
		self.neighbors = []
	
	def add_neighbor(self, n)
		self.neighbors.append(n)
	
	
class Graph:

	def __init__(self, nof_vertices, nof_edges):
		self.nof_vertices = nof_vertices
		self.nof_edges = nof_edges
		self.adjacency_matrix = np.matrix(np.zeros(shape=(nof_vertices, nof_vertices)), dtype=int)
		
	def add_edge(self, v1, v2):
		self.adjacency_matrix.itemset((v1, v2), 1)
		self.adjacency_matrix.itemset((v2, v1), 1)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	