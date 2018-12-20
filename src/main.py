from data_structures import Graph
from file_handler import FileHandler
from spectral_clustering import SpectralClustering
import numpy as np
import time
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tkinter

file_name = "ca-GrQc.txt"
input_path = "../graphs_part_1/"
output_path = "../out/"

file_handler = FileHandler()
graph = file_handler.r_file_to_graph(input_path + file_name)
sc = SpectralClustering(graph, file_handler.k)

def main():
	start_time = time.time()
	sc.compute_laplacian()
	print('Constructing Laplacian:  {}'.format(time.time() - start_time))
	start_time = time.time()
	sc.compute_eigenvectors_of_laplacian()
	print('Computing Eigenvectors:  {}'.format(time.time() - start_time))
	start_time = time.time()
	kmeans = sc.compute_clustering()
	print('Clustering:              {}'.format(time.time() - start_time))
	start_time = time.time()
	file_handler.create_output(output_path + file_name, graph, kmeans.labels_)
	print('Writing file:            {}'.format(time.time() - start_time))
	
	#print(graph.adjacency_matrix)
	#print(sc.laplacian_matrix)
	#print(sc.eigenvalues_of_laplacian)
	#print(sc.eigenvectors_of_laplacian)
	start_time = time.time()
	construct_image(kmeans.labels_)
	print('Image construction:      {}'.format(time.time() - start_time))
	print('---------------------------------------------')
	

def construct_image(labels):
	G = nx.from_numpy_array(graph.adjacency_matrix)
	coord = nx.spring_layout(G, iterations=20)
	fig = plt.figure()
	axs = fig.add_subplot(111, aspect='equal')
	axs.axis('off')
	nx.draw_networkx_edges(G, coord)
	nx.draw_networkx_nodes(G, coord, node_size=5, node_color=labels)
	plt.savefig("../img/graph.png")

start_time = time.time()
main()
print('Total:                   {}'.format(time.time() - start_time))

