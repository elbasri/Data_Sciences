import networkx as nx
import matplotlib.pyplot as plt

# Define the tasks and dependencies
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
    'N': {'duration': 6, 'dependencies': ['E']},
    'O': {'duration': 3, 'dependencies': ['F', 'G']},
    'P': {'duration': 2, 'dependencies': ['H']},
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

# Create a directed graph
G = nx.DiGraph()

# Add nodes with their durations as attributes
for task, info in tasks.items():
    G.add_node(task, duration=info['duration'])

# Add edges based on dependencies
for task, info in tasks.items():
    for dependency in info['dependencies']:
        G.add_edge(dependency, task)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=3500, node_color="skyblue")

# Draw edge labels
edge_labels = dict(((u, v), d['duration']) for u, v, d in G.edges(data=True))
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3)

# Show the graph
plt.show()
