from data_structures import Graph
from file_handler import FileHandler

file_path = "../graphs_part_1/ca-TestData.txt"
#file_path = "../graphs_part_1/ca-AstroPh.txt"
file_handler = FileHandler()

def main():
	graph = file_handler.r_file_to_graph(file_path)
	#print(graph.adjacency_matrix)
	
main()