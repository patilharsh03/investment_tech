from dolev_strong import Node, simulate_dolev_strong
from viz import draw_node_network

if __name__ == "__main__":
    draw_node_network(num_nodes=5, corrupt_nodes=[2])

# 5 nodes, with 1 corrupt
nodes = [Node(i, is_corrupt=(i == 2)) for i in range(5)]
results = simulate_dolev_strong(nodes, sender_input=1, f=1)

for node_id, output in results:
    print(f"Node {node_id} output: {output}")