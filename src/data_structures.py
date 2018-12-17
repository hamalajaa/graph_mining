import numpy as np
from scipy.sparse import csgraph
from numpy import linalg as la

"""

class Vertex:
	
	def __init__(self, idx):
		self.idx = idx
		self.neighbors = []
	
	def add_neighbor(self, n):
		self.neighbors.append(n)
	
"""
	
class Graph:

	def __init__(self, nof_vertices, nof_edges):
		self.nof_vertices = nof_vertices
		self.nof_edges = nof_edges
		self.adjacency_matrix = np.array(np.zeros(shape=(nof_vertices, nof_vertices)), dtype=int)
		self.laplacian_matrix = np.array(np.zeros(shape=(nof_vertices, nof_vertices)), dtype=int)
		self.eigenvalues_of_laplacian = np.array(np.zeros(shape=(nof_vertices, 1)), dtype=int)
		self.eigenvectors_of_laplacian = np.array(np.zeros(shape=(nof_vertices, nof_vertices)), dtype=int)
		
	def add_edge(self, v1, v2):
		self.adjacency_matrix.itemset((v1, v2), 1)
		self.adjacency_matrix.itemset((v2, v1), 1)
	
	def compute_laplacian(self):
		self.laplacian_matrix = csgraph.laplacian(self.adjacency_matrix, normed=True)
	
	def compute_eigenvectors_of_laplacian(self):
		self.eigenvalues_of_laplacian, self.eigenvectors_of_laplacian = la.eig(self.laplacian_matrix)
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	