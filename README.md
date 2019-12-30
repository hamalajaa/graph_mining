# Graph partition - Spectral clustering

## Setup

Install Python dependencies:
```
pip install -r requirements.txt
```

## Configuration

At /src/main.py you can change the file_name variable according the graph you want to partition. Graph-files should be located in /graphs_part_1/ in correct format.

## Performing the clustering

At /src, you can run the project simply with command
```
python main.py
```
which executes the program. The program outputs a text-file containing the clustering results for the given vertices. These files can be found in the /out -folder.

Executing the program also produces a simple 2d-visualization of the partitioned graph, which can be found from the /img -folder. These visualizations, however, aren't optimized to fit larger networks.

## Tests

The tests test only the correctness of the eigendecomposition of the Laplacian matrix. Tests can be run with the command
```
pytest
```
