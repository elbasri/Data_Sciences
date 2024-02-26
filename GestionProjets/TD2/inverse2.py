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

# Mise à jour des positions des nœuds pour les afficher dans l'ordre de A à M
pos = {task: (index, 0) for index, task in enumerate(sorted(tasks.keys()))}

plt.figure(figsize=(18, 5))  # Ajustement de la taille pour mieux voir l'ordre des tâches
for node in G.nodes():
    nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='red' if node in chemin_critique else 'skyblue', node_size=2000)
    nx.draw_networkx_labels(G, pos, labels={node: node for node in [node]})

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')

# Annotations pour chaque nœud
for node in pos:
    x, y = pos[node]
    plt.text(x, y-0.1, f"D: {G.nodes[node]['start']}, F: {G.nodes[node]['finish']}\nLS: {G.nodes[node]['late_start']}, LF: {G.nodes[node]['late_finish']}", ha='center', fontsize=8)

plt.title('Graphe CPM du Projet avec Chemin Critique et Annotations')
plt.axis('off')  # Cacher les axes pour un graphique plus propre
plt.show()

print(f"Durée totale du projet : {project_duree} unités de temps")
