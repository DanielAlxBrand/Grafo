import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
ciudades = ['Bogotá', 'Bucaramanga', 'Medellín', 'Cali', 'Barranquilla', 'Pasto']
aristas = [
    ('Bogotá', 'Bucaramanga', 395),
    ('Bogotá', 'Medellín', 415),
    ('Bogotá', 'Cali', 460),
    ('Bucaramanga', 'Barranquilla', 550),
    ('Medellín', 'Cali', 420),
    ('Medellín', 'Barranquilla', 710),
    ('Medellín', 'Pasto', 610),
    ('Cali', 'Pasto', 280)
]
for arista in aristas:
    G.add_edge(arista[0], arista[1], weight=arista[2])
camino_corto = nx.single_source_dijkstra_path(G, source='Bogotá')
distancia_corta = nx.single_source_dijkstra_path_length(G, source='Bogotá')
camino_corto_aristas = []
for ciudad, path in camino_corto.items():
    for i in range(len(path)-1):
        camino_corto_aristas.append((path[i], path[i+1]))
pos_real = {
    'Bogotá': (4.7, -74.1),
    'Bucaramanga': (7.1, -73.1),
    'Medellín': (6.2, -75.5),
    'Cali': (3.4, -76.5),
    'Barranquilla': (10.9, -74.8),
    'Pasto': (1.2, -77.3)
}
plt.figure(figsize=(10, 8))
# Dibujar todos los nodos y aristas en gris claro por defecto
nx.draw(G, pos_real, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='lightgray', arrows=True)

# Dibujar las aristas del camino más corto en rojo
nx.draw_networkx_edges(G, pos_real, edgelist=camino_corto_aristas, edge_color='red', width=3)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_real, edge_labels=labels, font_size=10)
color_map = ['lightcoral', 'lightgreen', 'lightblue', 'lightpink', 'lightyellow', 'lightsalmon']
nx.draw_networkx_nodes(G, pos_real, node_color=color_map, node_size=3000)
plt.title("Grafo de las distancias con el camino más corto resaltado (Dijkstra)")
plt.show()
