# BioSpecGT
Spectral graph theory for Biological network analysis

* Guarantees high-performance by using Cython
* Friendly interface
* ???
* Profit


## Usage
For the full documentation, see the [docs](https://requests.readthedocs.io/en/master/).

### Graph creation
 ```python
from BioSpecGT.graph.generator import complete_graph
g = complete_graph(n=100)
```

### Graph algorithms
 ```python
from BioSpecGT.graph.generator import complete_graph
from BioSpecGT.utils.graphutils import minimum_spanning_tree

g = complete_graph(n=100)
msp = minimum_spanning_tree(g)
```

### Spectral graph theory
```python
from BioSpecGT.linalg.spectral import laplacian_matrix
from BioSpecGT.graph.generator import k_regular_graph

g = k_regular_graph(n=100, k=20, selfloop=False)
l = laplacian_matrix(g)
```

### Spectral clustering
 ```python
from BioSpecGT.graph.generator import complete_graph
g = complete_graph(n=100)
```

### Importing datasets
 ```python
from BioSpecGT.graph.generator import complete_graph
g = complete_graph(n=100)
```

### Network analysis
 ```python
from BioSpecGT.graph.generator import complete_graph
g = complete_graph(n=100)
```


### Vizualization
 ```python
from BioSpecGT.graph.generator import complete_graph
g = complete_graph(n=100)
```
