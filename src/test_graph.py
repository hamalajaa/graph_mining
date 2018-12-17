from data_structures import Graph
from file_handler import FileHandler
import numpy as np
import pytest
from pytest import approx

#threshold = 0.00001
file_path = "../graphs_part_1/ca-TestData.txt"
file_handler = FileHandler()

def test_laplacian_eigenvectors():
	graph = file_handler.r_file_to_graph(file_path)
	graph.compute_laplacian()
	graph.compute_eigenvectors_of_laplacian()
	for i in range(graph.nof_vertices):
		assert(np.matmul(graph.laplacian_matrix, graph.eigenvectors_of_laplacian[:,i]) == approx(graph.eigenvalues_of_laplacian[i]	* graph.eigenvectors_of_laplacian[:,i]))
	