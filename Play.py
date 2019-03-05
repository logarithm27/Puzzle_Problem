import collections
from Node import *


class Play:
    def __init__(self, current_state):
        self.current_state = current_state

    def play(self):
        expansed = 0
        frontier = collections.deque([Node(self.current_state)])
        explored = set()
        explored.add(frontier[0].state)
        while frontier:
            frontier = collections.deque(sorted(list(frontier), key=lambda node: node.a_search))
            node = frontier.popleft()
            if node.solved:
                return [node.path, expansed]
            for move, action in node.actions:
                child = Node(move(), node, action)
                if child.state not in explored:
                    frontier.appendleft(child)
                    explored.add(child.state)
                    expansed += 1







