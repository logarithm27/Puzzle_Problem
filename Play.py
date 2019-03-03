from Numpy import matrix
from Numpy import *
from Utility import *
import numpy
from State import *


class ASearch:
    def __init__(self, current_state):
        self.g_function = 0
        self.h_function = 0
        self.f_function = 0
        self.parent_node = None
        self.child_node = None
        self.utility = Utility()
        self.current_state = current_state
        self.graph = {0: current_state}
        self.goal_state = generate_goal_state(len(self.current_state))
        self.possible_next_states = []
        self.matrix_to_number = {}
        self.first_state = State(self.heuristics(current_state), self.calculate_f_function(), self.g_function, None,
                                 current_state, from_matrix_to_number(self.current_state))
        self.path = []
        self.path.append(self.first_state)

    def calculate_f_function(self):
        self.f_function = self.g_function + self.h_function
        return self.f_function

    def heuristics(self, current_state):
        self.h_function = count_misplaced_blocks(current_state) + count_manhattan_distance(current_state)
        return self.h_function

    def next_states(self, current_state):
        self.parent_node = current_state
        self.g_function += 1
        self.utility.get_neighbor_buttons_of_blank_button(current_state)
        for element in self.utility.all_neighbors:
            next_move = self.move(current_state, element)
            state = State(self.heuristics(next_move), self.calculate_f_function(), self.g_function, current_state, next_move,
                          from_matrix_to_number(next_move))
            self.possible_next_states.append(state)
        current_state_to_number = from_matrix_to_number(current_state)
        self.matrix_to_number[current_state_to_number] = current_state
        return self.possible_next_states

    def move(self, new_state, down_up_left_right_value):
        state = []
        for line in new_state:
            for column in line:
                state.append(column)
        blank_block, block_where_to_move = state.index(0), state.index(down_up_left_right_value)
        state[blank_block], state[block_where_to_move] = state[block_where_to_move], state[blank_block]
        state = numpy.reshape(state, (len(new_state), len(new_state)))
        return state

    def is_goal_state(self, state):
        return numpy.allclose(state.state, self.goal_state)

    def breadth_first_search(self):
        frontier = list()
        explored = set()
        frontier.append(self.first_state)
        while frontier:
            state = frontier.pop(0)
            if self.is_goal_state(state):
                return explored
            explored.add(state)
            children = self.next_states(state.state)
            for child in children:
                if (child not in explored) or (child not in frontier):
                    frontier.append(child)
                    # levels[from_matrix_to_number(child)] = levels[from_matrix_to_number(state)]+1
        return None

a = ASearch(matrix(3))

print(a.breadth_first_search())







