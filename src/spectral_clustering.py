import numpy as np
from scipy.sparse import csgraph
from scipy.sparse import linalg as la
from sklearn.cluster import KMeans

class SpectralClustering:

	def __init__(self, graph, k):
		self.graph = graph
		self.k = k
		self.laplacian_matrix = np.array(np.zeros(shape=(graph.n, graph.n)), dtype=int)
		self.eigenvalues_of_laplacian = np.array(np.zeros(shape=(k, 1)), dtype=int)
		self.eigenvectors_of_laplacian = np.array(np.zeros(shape=(graph.n, k)), dtype=int)
		self.k_first_indices = np.array(np.zeros(shape=(k, 1)), dtype=int)

	def compute_laplacian(self):
		self.laplacian_matrix = csgraph.laplacian(self.graph.adjacency_matrix, normed=True)
			
		
	def compute_eigenvectors_of_laplacian(self):
		self.eigenvalues_of_laplacian, self.eigenvectors_of_laplacian = la.eigsh(self.laplacian_matrix, k=self.k, sigma=0, which='LM')
		
	def compute_clustering(self):
		return KMeans(n_clusters=self.k).fit(self.eigenvectors_of_laplacian)