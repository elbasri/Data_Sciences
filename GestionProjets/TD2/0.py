import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
tasks = {
    'A': {'duration': 2, 'dependencies': []},
    'B': {'duration': 18, 'dependencies': []},
    'C': {'duration': 1, 'dependencies': []},
    'D': {'duration': 2, 'dependencies': []},
    'E': {'duration': 6, 'dependencies': ['A']},
    'F': {'duration': 1, 'dependencies': ['A']},
    'G': {'duration': 0.5, 'dependencies': ['B']},
    'H': {'duration': 10, 'dependencies': ['B']},
    'I': {'duration': 12, 'dependencies': ['B']},
    'J': {'duration': 1.5, 'dependencies': ['C']},
    'K': {'duration': 3.5, 'dependencies': ['D']},
    'L': {'duration': 1.5, 'dependencies': ['D']},
    'M': {'duration': 6, 'dependencies': ['D']},
    'N': {'duration': 4.5, 'dependencies': []},
    'O': {'duration': 6, 'dependencies': ['E']},
    'P': {'duration': 3, 'dependencies': ['H']},
    'Q': {'duration': 10, 'dependencies': ['I']},
    'R': {'duration': 1.5, 'dependencies': ['J', 'K']},
    'S': {'duration': 6, 'dependencies': ['L']},
    'T': {'duration': 4.5, 'dependencies': ['N']},
    'U': {'duration': 0.5, 'dependencies': ['O']},
    'V': {'duration': 3, 'dependencies': ['P']},
    'W': {'duration': 3, 'dependencies': ['S']},
    'X': {'duration': 2, 'dependencies': ['M', 'Q', 'R', 'W']},
    'Y': {'duration': 1, 'dependencies': ['X']}
}


# Add nodes with durations as attributes
for task, info in tasks.items():
    G.add_node(task, duration=info['duration'])

# Add edges from dependencies
for task, info in tasks.items():
    for dependency in info['dependencies']:
        G.add_edge(dependency, task)

# Compute the earliest start and finish times
for node in nx.topological_sort(G):
    preds = list(G.predecessors(node))
    if preds:
        G.nodes[node]['start'] = max(G.nodes[pred]['finish'] for pred in preds)
    else:
        G.nodes[node]['start'] = 0
    G.nodes[node]['finish'] = G.nodes[node]['start'] + G.nodes[node]['duration']

# The project duration is the maximum finish time
project_duration = max(nx.get_node_attributes(G, 'finish').values())

# Draw the graph
pos = nx.planar_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G.nodes[v]['start'] for u, v in G.edges()}, font_color='red')
plt.title('Graphe CPM du Projet de Chargement de l\'Avion')
plt.show()

project_duration
