


class State():
    def __init__(self, h_function, f_function, parent_node, state):
        self.g_function = 0
        self.h_function = h_function
        self.f_function = f_function
        self.parent_node = parent_node
        self.state = state
