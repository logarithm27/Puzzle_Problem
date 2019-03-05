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

    def create_move(self, at, to):
        return lambda: self._move(at, to)

    @property
    def actions(self):
        moves = []
        for line_index, column_index in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {' moved Left \u2190': (line_index, column_index-1),
                      ' moved Right \u2192': (line_index, column_index+1),
                      ' moved Up \u2191': (line_index-1, column_index),
                      ' moved Down \u2193': (line_index+1, column_index)}

            for action, (line, column) in direcs.items():
                if line >= 0 and column >= 0 and line < self.width and column < self.width and \
                        self.current_state[line][column] == 0:
                    move = self.create_move((line_index, column_index), (line, column)), action, \
                           str(self.current_state[line_index][column_index])
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

    # hashing the current state
    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.current_state:
            yield from row
