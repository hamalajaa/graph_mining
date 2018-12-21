import numpy as np
from scipy.sparse import csgraph
from scipy.sparse import linalg as la
from sklearn.cluster import KMeans
from sklearn import preprocessing

class SpectralClustering:

	def __init__(self, graph, k):
		self.graph = graph
		self.k = k
		self.laplacian_matrix = np.array(np.zeros(shape=(graph.n, graph.n)), dtype=int)
		self.eigenvalues_of_laplacian = np.array(np.zeros(shape=(k, 1)), dtype=int)
		self.eigenvectors_of_laplacian = np.array(np.zeros(shape=(graph.n, k)), dtype=int)
		self.normalized_eigenvectors = np.array(np.zeros(shape=(graph.n, k)), dtype=int)
		self.k_first_indices = np.array(np.zeros(shape=(k, 1)), dtype=int)
		self.labels = np.array([])

	def compute_laplacian(self):
		self.laplacian_matrix = csgraph.laplacian(self.graph.adjacency_matrix, normed=True)
		
	def compute_eigenvectors_of_laplacian(self):
		self.eigenvalues_of_laplacian, self.eigenvectors_of_laplacian = la.eigsh(self.laplacian_matrix, k=self.k, sigma=0, which='LM')
		for i in range(self.graph.n):
			self.eigenvectors_of_laplacian[i] = preprocessing.normalize([self.eigenvectors_of_laplacian[i]], norm='l2')
		
	def compute_clustering(self):
		kmeans = KMeans(n_clusters=self.k).fit(self.eigenvectors_of_laplacian)
		self.labels = kmeans.labels_
		return kmeans
		
	
	def goodness_of_partition(self):
		cut_edges = 0
		community_sizes = np.array(np.zeros(shape=(self.k, 1)), dtype=int)
		for i in range(self.graph.n):
			li = self.labels[i]
			community_sizes[li] += 1
			for j in range(i, self.graph.n):
				if self.graph.adjacency_matrix.item(i, j) is 1 and li != self.labels.item(j):
					cut_edges += 1
		return cut_edges, min(community_sizes), max(community_sizes)
	
		