from Numpy import matrix
from Numpy import *
from Utility import *
import numpy


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

    def calculate_f_function(self):
        self.f_function = self.g_function + self.h_function

    def heuristics(self, current_state):
        self.h_function = count_misplaced_blocks(current_state) + count_manhattan_distance(current_state)

    def next_states(self, current_state):
        self.parent_node = current_state
        self.utility.get_neighbor_buttons_of_blank_button(current_state)
        for element in self.utility.all_neighbors:
            self.possible_next_states.append(self.move(current_state, element))
        current_state_to_number = from_matrix_to_number(current_state)
        self.matrix_to_number[current_state_to_number] = current_state
        return self.possible_next_states

    def move(self, new_state, down_up_left_right_value):
        numpy.place(new_state, new_state == down_up_left_right_value, -2)
        numpy.place(new_state, new_state == 0, down_up_left_right_value)
        numpy.place(new_state, new_state == -2, 0)
        return new_state

    def is_goal_state(self, state):
        return state == self.goal_state

    def breadth_first_search(self):
        initial_state = self.current_state
        # if self.is_goal_state(initial_state):
        #     return initial_state
        frontier = list()
        explored = set()
        current_state_to_number = from_matrix_to_number(initial_state)
        levels = {current_state_to_number: 0}
        frontier.append(initial_state)
        while frontier:
            state = frontier.pop(0)
            # if self.is_goal_state(state):
            #     return state
            explored.add(from_matrix_to_number(state))
            children = self.next_states(state)
            for child in children:
                if (from_matrix_to_number(child) not in explored) or (child not in frontier):
                    frontier.append(child)
                    levels[from_matrix_to_number(child)] = levels[from_matrix_to_number(state)]+1
        return explored

search = ASearch(matrix(3))

print(search.breadth_first_search())






