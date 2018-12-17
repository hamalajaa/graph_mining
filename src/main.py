from data_structures import Graph
from file_handler import FileHandler
from spectral_clustering import SpectralClustering
import numpy as np
import timeit
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tkinter


file_path = "../graphs_part_1/ca-GrQc.txt"
#file_path = "../graphs_part_1/ca-hepTh.txt"
#file_path = "../graphs_part_1/ca-TestData.txt"
file_handler = FileHandler()
graph = file_handler.r_file_to_graph(file_path)
sc = SpectralClustering(graph, file_handler.k)

def main():
	sc.compute_laplacian()
	sc.compute_eigenvectors_of_laplacian()
	kmeans = sc.compute_clustering()
	#print(graph.adjacency_matrix)
	#print(sc.laplacian_matrix)
	#print(sc.eigenvalues_of_laplacian)
	#print(sc.eigenvectors_of_laplacian)
	construct_image(kmeans.labels_)
	

def construct_image(labels):
	G = nx.from_numpy_array(graph.adjacency_matrix)
	coord = nx.spring_layout(G, iterations=100)
	fig = plt.figure()
	axs = fig.add_subplot(111, aspect='equal')
	axs.axis('off')
	nx.draw_networkx_edges(G, coord)
	nx.draw_networkx_nodes(G, coord, node_size=5, node_color=labels)
	plt.savefig("../img/graph.png")


print(timeit.Timer(main).timeit(number=1))
