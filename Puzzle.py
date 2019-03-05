import itertools
from Numpy import *


class Puzzle:

    def __init__(self, current_state):
        self.width = len(current_state[0])
        self.current_state = current_state

    @property
    def solved(self):
        puzzle_length = self.width * self.width
        return str(self) == ''.join(map(str, range(1, puzzle_length))) + '0'

    @property
    def actions(self):
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'Right Move': (i, j-1),
                      'Left Move': (i, j+1),
                      'Down Move': (i-1, j),
                      'Up Move': (i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                        self.current_state[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    @property
    def heuristics(self):
        return count_manhattan_distance_and_misplaced_blocks(self.current_state)

    def copy(self):
        current_state = []
        for row in self.current_state:
            current_state.append([x for x in row])
        return Puzzle(current_state)

    def _move(self, at, to):
        copy = self.copy()
        i, j = at
        r, c = to
        copy.current_state[i][j], copy.current_state[r][c] = copy.current_state[r][c], copy.current_state[i][j]
        return copy

    def print_state(self):
        for row in self.current_state:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.current_state:
            yield from row
