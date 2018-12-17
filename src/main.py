from data_structures import Graph
from file_handler import FileHandler
import numpy as np

file_path = "../graphs_part_1/ca-TestData.txt"
#file_path = "../graphs_part_1/ca-AstroPh.txt"
file_handler = FileHandler()

def main():
	graph = file_handler.r_file_to_graph(file_path)
	graph.compute_laplacian()
	graph.compute_eigenvectors_of_laplacian()
	print(graph.adjacency_matrix)
	print(graph.laplacian_matrix)
	print(graph.eigenvalues_of_laplacian)
	print(graph.eigenvectors_of_laplacian)
	
	
main()