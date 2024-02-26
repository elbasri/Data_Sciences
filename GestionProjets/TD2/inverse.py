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

for node in G.nodes:
    G.nodes[node]['late_finish'] = float('inf')
    G.nodes[node]['late_start'] = float('inf')

project_duree = max(nx.get_node_attributes(G, 'finish').values())

for node in reversed(list(nx.topological_sort(G))):
    succs = list(G.successors(node))
    if succs:
        G.nodes[node]['late_finish'] = min(G.nodes[succ]['late_start'] for succ in succs)
    else:
        G.nodes[node]['late_finish'] = project_duree
    G.nodes[node]['late_start'] = G.nodes[node]['late_finish'] - G.nodes[node]['duree']

chemin_critique = [node for node in G.nodes if G.nodes[node]['start'] == G.nodes[node]['late_start']]

pos = nx.spring_layout(G, k=2, iterations=20)

plt.figure(figsize=(15, 10))
node_colors = ['red' if node in chemin_critique else 'skyblue' for node in G.nodes()]
nx.draw(G, pos, with_labels=False, node_size=2000, node_color=node_colors, font_size=12, font_weight='bold')
edge_colors = ['red' if u in chemin_critique and v in chemin_critique else 'black' for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)

# Annotations pour début, fin, late start et late finish
for node in G.nodes:
    label = f"{node}\nD: {G.nodes[node]['start']}, F: {G.nodes[node]['finish']}\nLS: {G.nodes[node]['late_start']}, LF: {G.nodes[node]['late_finish']}"
    x, y = pos[node]
    plt.text(x, y+0.1, label, fontsize=8, ha='center')

plt.title('Graphe CPM du Projet avec Chemin Critique et Annotations')
plt.axis('off')
plt.show()

print(f"Durée totale du projet : {project_duree} unités de temps")
