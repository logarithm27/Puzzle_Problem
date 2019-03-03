


class State():
    def __init__(self, h_function, f_function, g_function, parent_node, state, hash):
        self.g_function = g_function
        self.h_function = h_function
        self.f_function = f_function
        self.parent_node = parent_node
        self.state = state
        self.children = None
        self.hash = hash
