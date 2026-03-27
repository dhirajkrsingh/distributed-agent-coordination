# Distributed Agent Coordination

> **Algorithms and patterns for coordinating agents across distributed systems.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

Distributed coordination is one of the hardest problems in multi-agent systems. How do agents agree on a plan? How do they allocate tasks without a central controller? This repo covers the core algorithms and patterns.

## Topics Covered

| Algorithm | Category | Description |
|-----------|----------|-------------|
| **Leader Election** | Consensus | Agents elect a coordinator dynamically |
| **Task Auction** | Allocation | Distributed task assignment via bidding |
| **Consensus Protocol** | Agreement | Agents converge on a shared value |
| **Mutual Exclusion** | Coordination | Ensure only one agent accesses a resource |

## Examples

| File | Description |
|------|-------------|
| [`examples/01_leader_election.py`](examples/01_leader_election.py) | Bully algorithm for leader election |
| [`examples/02_task_auction.py`](examples/02_task_auction.py) | Distributed task allocation via auctions |
| [`examples/03_consensus.py`](examples/03_consensus.py) | Agents reaching agreement on a value |

## Best Practices

1. **Assume failures** — Any agent can crash at any time; design for it
2. **Use timeouts** — Don't wait forever for a response
3. **Idempotent operations** — Operations that can be safely retried
4. **Avoid single points of failure** — Distribute coordination responsibility
5. **Prefer eventual consistency** — Strict consistency is expensive in distributed systems

## Getting Started

```bash
git clone https://github.com/dhirajkrsingh/distributed-agent-coordination.git
cd distributed-agent-coordination
python examples/01_leader_election.py
```

## References

| Resource | Description |
|----------|-------------|
| [Raft Consensus](https://raft.github.io/) | Understandable consensus algorithm |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Distributed agent conversations |
| [ray-project/ray](https://github.com/ray-project/ray) | Distributed computing framework |
| [Distributed Systems by Tanenbaum](https://www.distributed-systems.net/) | Classic textbook |

---

**Author:** [Dhiraj Kumar Singh](https://github.com/dhirajkrsingh) — AI Trainer
