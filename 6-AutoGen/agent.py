from planner import plan
from tools import search_tool
from memory import Memory


class AutoAgent:

    def __init__(self, goal):
        self.goal = goal
        self.memory = Memory()

    def run(self):

        for step in range(5):

            history = self.memory.get()

            decision = plan(self.goal, history)

            print("\nAgent Thought:", decision)

            if "search" in decision.lower() or "ara" in decision.lower():

                result = search_tool(self.goal)

                print("\nSearch Result:", result[:500])

                self.memory.add(result)

            else:
                self.memory.add(decision)

        return self.memory.logs