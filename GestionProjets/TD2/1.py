import networkx as nx
import matplotlib.pyplot as plt

tasks = {
    'A': {'duree': 8, 'dependencies': []},
    'B': {'duree': 10, 'dependencies': ['A']},
    'C': {'duree': 6, 'dependencies': ['A']},
    'D': {'duree': 12, 'dependencies': ['B']},
    'E': {'duree': 12, 'dependencies': ['C']},
    'F': {'duree': 6, 'dependencies': ['B']},
    'G': {'duree': 8, 'dependencies': ['C']},
    'H': {'duree': 6, 'dependencies': ['D', 'E']},
    'I': {'duree': 12, 'dependencies': ['D', 'E']},
    'J': {'duree': 8, 'dependencies': ['F', 'G']},
    'K': {'duree': 14, 'dependencies': ['J']},
    'L': {'duree': 8, 'dependencies': ['H', 'K']},
    'M': {'duree': 7, 'dependencies': ['L']},
}

G = nx.DiGraph()

for task, info in tasks.items():
    G.add_node(task, duree=info['duree'])

for task, info in tasks.items():
    for dependency in info['dependencies']:
        G.add_edge(dependency, task)

for node in nx.topological_sort(G):
    preds = list(G.predecessors(node))
    if preds:
        G.nodes[node]['start'] = max(G.nodes[pred]['finish'] for pred in preds)
    else:
        G.nodes[node]['start'] = 0
    G.nodes[node]['finish'] = G.nodes[node]['start'] + G.nodes[node]['duree']

project_duree = max(nx.get_node_attributes(G, 'finish').values())

pos = nx.planar_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G.nodes[v]['start'] for u, v in G.edges()}, font_color='red')
plt.title('Graphe CPM du Projet')
plt.show()

project_duree
