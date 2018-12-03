from data_structures import Graph




class FileHandler:

	def __init__(self):
		self.data = []
	
	
	#Reads an input file given as parameter and constructs a graph based on the data.
	
	def r_file_to_graph(self, input_file):
		file = open(input_file, "r")
		header = (file.readline()).split()
		nof_vertices = int(header[2])
		nof_edges = int(header[3])
		graph = Graph(nof_vertices, nof_edges)
		for line in file:
			vertices = line.split()
			graph.add_edge(int(vertices[0]), int(vertices[1]))
		return graph
		
	#def w_graph_to_file(self, output_file, graph):
		
		