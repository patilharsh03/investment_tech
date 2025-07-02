import matplotlib.pyplot as plt
import networkx as nx

def draw_node_network(num_nodes, corrupt_nodes=None):
    if corrupt_nodes is None:
        corrupt_nodes = []

    G = nx.complete_graph(num_nodes)
    pos = nx.circular_layout(G)

    color_map = [
        'red' if node in corrupt_nodes else 'lightblue'
        for node in G.nodes()
    ]

    labels = {node: f"Node {node}" for node in G.nodes()}

    nx.draw(
        G, pos, labels=labels,
        node_color=color_map, node_size=1200,
        font_size=10, edge_color='gray'
    )

    plt.title("Byzantine Broadcast Node Network\n(Red = Corrupt Nodes)")
    plt.axis('off')
    plt.show()