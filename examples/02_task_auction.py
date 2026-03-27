"""
Example 2: Distributed Task Auction
=====================================
Agents bid on tasks based on their capabilities and current load.
Tasks are assigned to the best bidder without a central controller.

Run: python examples/02_task_auction.py
"""

import random


class AuctioneerAgent:
    """Announces tasks and selects winners based on bids."""

    def __init__(self, name: str):
        self.name = name
        self.assignments = {}

    def auction_task(self, task: dict, bidders: list) -> str:
        print(f"\n  [{self.name}] Auctioning: '{task['name']}' (priority: {task['priority']})")

        bids = []
        for bidder in bidders:
            bid = bidder.make_bid(task)
            if bid is not None:
                bids.append((bidder.name, bid))
                print(f"    [{bidder.name}] Bids: score={bid:.2f}")
            else:
                print(f"    [{bidder.name}] Cannot bid (overloaded)")

        if not bids:
            print(f"  [{self.name}] No valid bids. Task unassigned.")
            return "UNASSIGNED"

        # Select winner (highest score = best fit)
        winner_name, best_score = max(bids, key=lambda x: x[1])
        self.assignments[task["name"]] = winner_name

        # Notify winner
        for bidder in bidders:
            if bidder.name == winner_name:
                bidder.accept_task(task)
                break

        print(f"  [{self.name}] Assigned '{task['name']}' to {winner_name} (score: {best_score:.2f})")
        return winner_name


class WorkerAgent:
    """Bids on and executes tasks."""

    def __init__(self, name: str, capacity: int, skills: list):
        self.name = name
        self.capacity = capacity
        self.current_load = 0
        self.skills = skills
        self.assigned_tasks = []

    def make_bid(self, task: dict):
        if self.current_load >= self.capacity:
            return None  # Overloaded

        # Score based on skill match and available capacity
        skill_match = len(set(self.skills) & set(task.get("required_skills", [])))
        available = self.capacity - self.current_load
        noise = random.uniform(0.9, 1.1)
        return (skill_match * 10 + available * 2) * noise

    def accept_task(self, task: dict):
        self.assigned_tasks.append(task["name"])
        self.current_load += 1
        print(f"    [{self.name}] Accepted '{task['name']}' (load: {self.current_load}/{self.capacity})")


if __name__ == "__main__":
    print("=== Distributed Task Auction Demo ===")

    auctioneer = AuctioneerAgent("Auctioneer")

    workers = [
        WorkerAgent("ML-Agent", capacity=3, skills=["python", "ml", "data"]),
        WorkerAgent("Web-Agent", capacity=2, skills=["javascript", "api", "html"]),
        WorkerAgent("DevOps-Agent", capacity=2, skills=["docker", "k8s", "cicd"]),
        WorkerAgent("Fullstack-Agent", capacity=3, skills=["python", "javascript", "api"]),
    ]

    tasks = [
        {"name": "Train Model", "priority": "high", "required_skills": ["python", "ml"]},
        {"name": "Build REST API", "priority": "medium", "required_skills": ["python", "api"]},
        {"name": "Setup CI/CD", "priority": "high", "required_skills": ["docker", "cicd"]},
        {"name": "Create Dashboard", "priority": "low", "required_skills": ["javascript", "html"]},
        {"name": "Data Pipeline", "priority": "high", "required_skills": ["python", "data"]},
    ]

    for task in tasks:
        auctioneer.auction_task(task, workers)

    print("\n=== Final Assignments ===")
    for task_name, worker_name in auctioneer.assignments.items():
        print(f"  {task_name} -> {worker_name}")
