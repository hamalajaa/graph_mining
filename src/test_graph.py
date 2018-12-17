from data_structures import Graph
from file_handler import FileHandler
from spectral_clustering import SpectralClustering
import numpy as np
import pytest
from pytest import approx

flat_tol = 0.001
rel_tol = 0.00001
file_path = "../graphs_part_1/ca-GrQc.txt"
file_handler = FileHandler()
graph = file_handler.r_file_to_graph(file_path)
sc = SpectralClustering(graph, file_handler.k)

def test_laplacian_eigenvectors():
	sc.compute_laplacian()
	sc.compute_eigenvectors_of_laplacian()
	for i in range(sc.k):
		assert np.allclose(np.matmul(sc.laplacian_matrix, sc.eigenvectors_of_laplacian[:,i]), sc.eigenvalues_of_laplacian[i] * sc.eigenvectors_of_laplacian[:,i], atol=flat_tol, rtol=rel_tol)
	