from data_structures import Graph
from file_handler import FileHandler
from spectral_clustering import SpectralClustering
import numpy as np
import timeit

file_path = "../graphs_part_1/ca-GrQc.txt"
#file_path = "../graphs_part_1/ca-hepTh.txt"
#file_path = "../graphs_part_1/ca-TestData.txt"
file_handler = FileHandler()
graph = file_handler.r_file_to_graph(file_path)
sc = SpectralClustering(graph, file_handler.k)

def main():
	sc.compute_laplacian()
	sc.compute_eigenvectors_of_laplacian()
	print(graph.adjacency_matrix)
	print(sc.laplacian_matrix)
	print(sc.eigenvalues_of_laplacian)
	print(sc.eigenvectors_of_laplacian)
	
#main()
print(timeit.Timer(main).timeit(number=1))
