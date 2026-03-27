"""
Example 1: Leader Election (Bully Algorithm)
==============================================
Agents with unique IDs elect a leader. The agent with the highest ID becomes leader.
If the leader fails, a new election is triggered automatically.

Run: python examples/01_leader_election.py
"""

import random


class DistributedAgent:
    """An agent that participates in leader election."""

    def __init__(self, agent_id: int):
        self.agent_id = agent_id
        self.alive = True
        self.leader_id = None
        self.peers = []

    def set_peers(self, peers: list):
        self.peers = [p for p in peers if p.agent_id != self.agent_id]

    def start_election(self):
        """Bully algorithm: contact all agents with higher IDs."""
        print(f"  [Agent-{self.agent_id}] Starting election...")
        higher_agents = [p for p in self.peers if p.agent_id > self.agent_id and p.alive]

        if not higher_agents:
            # No higher agent alive — I am the leader
            self.declare_victory()
            return

        # Send election message to higher agents
        for agent in higher_agents:
            response = agent.receive_election(self.agent_id)
            if response == "OK":
                print(f"  [Agent-{self.agent_id}] Got OK from Agent-{agent.agent_id}, standing down.")
                return  # A higher agent will take over

    def receive_election(self, from_id: int) -> str:
        """Respond to an election message from a lower-ID agent."""
        if not self.alive:
            return "NO_RESPONSE"
        print(f"  [Agent-{self.agent_id}] Received election from Agent-{from_id}, responding OK")
        self.start_election()  # Trigger my own election
        return "OK"

    def declare_victory(self):
        """Announce this agent as the new leader."""
        print(f"  [Agent-{self.agent_id}] I am the NEW LEADER!")
        self.leader_id = self.agent_id
        for peer in self.peers:
            if peer.alive:
                peer.leader_id = self.agent_id


def simulate_failure(agents: list, agent_id: int):
    """Simulate an agent crash."""
    for a in agents:
        if a.agent_id == agent_id:
            a.alive = False
            print(f"\n  [SYSTEM] Agent-{agent_id} has CRASHED!")
            break


if __name__ == "__main__":
    print("=== Leader Election (Bully Algorithm) ===\n")

    # Create agents with unique IDs
    agents = [DistributedAgent(i) for i in range(1, 6)]
    for a in agents:
        a.set_peers(agents)

    # Initial election: lowest agent starts
    agents[0].start_election()
    print(f"\n  Current leader: Agent-{agents[0].leader_id}\n")

    # Simulate leader crash
    simulate_failure(agents, 5)

    # Agent 2 detects failure and starts new election
    print()
    agents[1].start_election()
    print(f"\n  New leader: Agent-{agents[1].leader_id}")
