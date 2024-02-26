import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the tasks, durations, and dependencies
tasks_data = """
Code,Tâches,Antécédents,Durées
A,Tri des documents de colis,-,2
B,Enregistrer les passagers,-,18
C,Préparer les escabeaux,-,1
D,Mettre en place l'avion,-,2
E,Établir les états de colisage,A,6
F,Rassembler documents en sacoches,A,1
G,Transmettre le nombre de passagers,B,0.5
H,Peser et étiqueter les bagages,B,10
I,Formalités douane et police,B,12
J,Mise en place des escabeaux,C,1.5
K,Embarquer les repas,D,3.5
L,Mettre en place le groupe de démarrage sous l'avion,D,1.5
M,Faire le plein de carburant,D,6
N,Trier les colis à embarquer,E,6
O,Compléter sacoche de documents,F,G,3
P,Prise en charge bagages sur chariots,H,2
Q,Attente passagers en salle de départ,I,10
R,Embarquer hôtesses et stewards,J,K,1.5
S,Contrôles du mécanicien,L,6
T,Charger les colis en soute,N,4.5
U,Mise à bord des documents,O,0.5
V,Charger les bagages,P,3
W,Mise en place de l'équipage,S,3
X,Embarquer les passagers,M,Q,R,W,2
Y,Installation des passagers à bord,X,1
"""

# Load the data into a DataFrame
df_tasks = pd.read_csv(StringIO(tasks_data))

# Create a Directed Acyclic Graph (DAG) for the tasks
G = nx.DiGraph()

# Add nodes with durations as attributes
for index, row in df_tasks.iterrows():
    G.add_node(row['Code'], duration=row['Durées'])

# Add edges from dependencies
for index, row in df_tasks.iterrows():
    dependencies = str(row['Antécédents']).split(',')
    for dep in dependencies:
        if dep != '-':
            G.add_edge(dep.strip(), row['Code'])

# Compute the earliest start and finish times
for node in nx.topological_sort(G):
    preds = list(G.predecessors(node))
    if preds:
        G.nodes[node]['start'] = max(G.nodes[pred]['finish'] for pred in preds)
    else:
        G.nodes[node]['start'] = 0
    G.nodes[node]['finish'] = G.nodes[node]['start'] + G.nodes[node]['duration']

# Calculate the latest start and finish times
for node in reversed(list(nx.topological_sort(G))):
    succs = list(G.successors(node))
    if succs:
        G.nodes[node]['latest_finish'] = min(G.nodes[succ]['latest_start'] for succ in succs)
    else:
        G.nodes[node]['latest_finish'] = G.nodes[node]['finish']
    G.nodes[node]['latest_start'] = G.nodes[node]['latest_finish'] - G.nodes[node]['duration']

# Identify the critical path
critical_path = [node for node in nx.topological_sort(G) if G.nodes[node]['start'] == G.nodes[node]['latest_start']]

# Draw the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G.nodes[v]['start'] for u, v in G.edges()}, font_color='red')
plt.title('Graphe CPM des opérations de chargement')
plt.show()

# Display critical path and project duration
project_duration = G.nodes[critical_path[-1]]['finish']
critical_path, project_duration
