from collections import defaultdict
from typing import List, Dict, Set

class Node:
    def __init__(self, node_id: int, is_corrupt: bool = False):
        self.node_id = node_id
        self.is_corrupt = is_corrupt
        self.extracted: Set[int] = set()
        self.received: Dict[int, List[List[int]]] = defaultdict(list)

    def receive(self, message: List[int]):
        sig_set = tuple(sorted(message))
        if sig_set not in self.received[len(message)]:
            self.received[len(message)].append(sig_set)
            if message[0] not in self.extracted:
                self.extracted.add(message[0])
                return message + [self.node_id]
        return None

def simulate_dolev_strong(nodes: List[Node], sender_input: int, f: int):
    rounds = f + 1
    messages = {0: [[sender_input, 0]]}  # round 0 message from sender (node 0)

    for r in range(1, rounds + 1):
        messages[r] = []
        for node in nodes:
            for msg in messages[r - 1]:
                new_msg = node.receive(msg)
                if new_msg:
                    messages[r].append(new_msg)

    outputs = []
    for node in nodes:
        if len(node.extracted) == 1:
            outputs.append((node.node_id, list(node.extracted)[0]))
        else:
            outputs.append((node.node_id, 0))  # default to 0
    return outputs