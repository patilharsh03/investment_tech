from market_sim.consensus.dolev_strong import Node, simulate_dolev_strong

def test_dotenv_strong_agreement():
    nodes = [Node(i, is_corrupt=(i == 2)) for i in range(5)]
    outputs = simulate_dolev_strong(nodes, sender_input=1, f=1)
    values = set(value for _, value in outputs)
    assert len(values) == 1
    assert 1 in values