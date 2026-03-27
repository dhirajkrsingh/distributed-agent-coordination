"""
Example 3: Consensus Protocol
===============================
Agents start with different values and iteratively converge to agreement.
Implements a simplified average-consensus algorithm.

Run: python examples/03_consensus.py
"""

import random


class ConsensusAgent:
    """An agent that participates in distributed consensus."""

    def __init__(self, name: str, initial_value: float):
        self.name = name
        self.value = initial_value
        self.neighbors = []

    def add_neighbor(self, agent):
        self.neighbors.append(agent)

    def update(self) -> float:
        """Average own value with neighbors' values."""
        if not self.neighbors:
            return self.value
        neighbor_values = [n.value for n in self.neighbors]
        all_values = [self.value] + neighbor_values
        new_value = sum(all_values) / len(all_values)
        return new_value


def run_consensus(agents: list, max_rounds: int = 20, tolerance: float = 0.01):
    """Run consensus rounds until convergence or max iterations."""
    print("  Initial values:")
    for a in agents:
        print(f"    {a.name}: {a.value:.4f}")

    for round_num in range(1, max_rounds + 1):
        # Compute new values (synchronous update)
        new_values = {a.name: a.update() for a in agents}

        # Apply updates
        for a in agents:
            a.value = new_values[a.name]

        values = [a.value for a in agents]
        spread = max(values) - min(values)

        if round_num % 3 == 0 or spread < tolerance:
            print(f"\n  Round {round_num}: spread={spread:.6f}")
            for a in agents:
                print(f"    {a.name}: {a.value:.4f}")

        if spread < tolerance:
            print(f"\n  Consensus reached in {round_num} rounds!")
            print(f"  Agreed value: {sum(values)/len(values):.4f}")
            return

    print(f"\n  Max rounds reached. Final spread: {spread:.6f}")


if __name__ == "__main__":
    print("=== Distributed Consensus Demo ===\n")

    # Create agents with random initial values
    agents = [
        ConsensusAgent("Sensor-A", random.uniform(10, 50)),
        ConsensusAgent("Sensor-B", random.uniform(10, 50)),
        ConsensusAgent("Sensor-C", random.uniform(10, 50)),
        ConsensusAgent("Sensor-D", random.uniform(10, 50)),
        ConsensusAgent("Sensor-E", random.uniform(10, 50)),
    ]

    # Create a ring topology: each agent talks to its neighbors
    for i in range(len(agents)):
        agents[i].add_neighbor(agents[(i - 1) % len(agents)])
        agents[i].add_neighbor(agents[(i + 1) % len(agents)])

    run_consensus(agents)
