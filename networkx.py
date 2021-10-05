import networkx as nx
import matplotlib.pyplot as mat

G=nx.Graph()

G.add_node(1)

G.add_node(2)
G.add_node(3)

G.add_edge(1,2)
G.add_edge(3,2)
G.add_edge(1,3)
nx.draw(G)
mat.show()
