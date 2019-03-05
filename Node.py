from Puzzle import *


class Node:
    def __init__(self, current_state, parent=None, action=None):
        self.current_state = current_state
        self.parent = parent
        self.action = action
        if self.parent is not None:
            self.bfs_search = parent.bfs_search + 1
        else:
            self.bfs_search = 0

    @property
    def score(self):
        return self.bfs_search + self.heuristic

    @property
    def state(self):
        return str(self)

    @property
    def path(self):
        node, node_is_parent_of = self, []
        while node:
            node_is_parent_of.append(node)
            node = node.parent
        yield from reversed(node_is_parent_of)

    @property
    def solved(self):
        return self.current_state.solved

    @property
    def actions(self):
        return self.current_state.actions

    @property
    def heuristic(self):
        return self.current_state.heuristics

    @property
    def a_search(self):
        return self.heuristic + self.bfs_search

    def __str__(self):
        return str(self.current_state)


